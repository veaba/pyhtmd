# 解析器
import re
# remove_attrs, \
from .utils import remove_parent_wrap, \
    remove_span, \
    br_to_newline, \
    br_to_empty, \
    remove_attrs_value, \
    remove_custom, \
    remove_p, \
    remove_nbsp, \
    remove_list_whitespace, \
    is_has_child, \
    get_tag_text, \
    get_tag_name, \
    get_href, \
    get_src, get_alt, clean_up, \
    get_right_index, \
    is_ol, \
    is_ul

# ***************************解析部分************************
# 将获取被包围的node节点解析成为数组 Given a tensor <code translate="no"
# dir="ltr">t<\/code>, this operation returns a tensor of the same type  andshape as <code translate="no"
# dir="ltr">t<\/code> with its values clipped to <code translate="no" dir="ltr">clip_value_min<\/code> and <code
# translate="no" dir="ltr">clip_value_max</code>.Any values less than <code translate="no"
# parser_bdir="ltr">clip_value_min</code> are set to <code translate="no" dir="ltr">clip_value_min</code>. Any
# valuesgreater than <code translate="no" dir="ltr">clip_value_max</code> are set to <code translate="no"
# dir="ltr">clip_value_max</code>. ===> re.finditer(r'<(.*?)(>)(.*?)(<\/(.*?)>)', h)
"""
<code translate="no" dir="ltr">t</code>
<code translate="no" dir="ltr">t</code>
<code translate="no" dir="ltr">clip_value_min</code>
<code translate="no" dir="ltr">clip_value_max</code>
<code translate="no" dir="ltr">clip_value_min</code>
<code translate="no" dir="ltr">clip_value_min</code>
<code translate="no" dir="ltr">clip_value_max</code>
<code translate="no" dir="ltr">clip_value_max</code>
"""


class Pip:
    def __init__(self, block=""):
        self.block = block
        self.factory()

    # 工厂函数
    def factory(self):
        block_content = self.__a_pip(self, self.block)
        block_content = self.__p_pip(self, block_content)
        block_content = self.__b_pip(self, block_content)
        block_content = self.__strong_pip(self, block_content)
        block_content = self.__img_pip(self, block_content)
        block_content = self.__pre_pip(self, block_content)
        block_content = self.__code_pip(self, block_content)
        block_content = self.__em_pip(self, block_content)
        block_content = remove_custom(block_content)
        block_content = remove_nbsp(block_content)
        block_content = remove_p(block_content)
        return block_content

    @staticmethod
    def __a_pip(self, block):
        block_content = block
        a_blocks = re.finditer(r'<a(.*?)</a>', block)
        for item in a_blocks:
            content = item.group()
            block_content = block_content.replace(content, parser_a(content))
        return block_content

    @staticmethod
    def __p_pip(self, block):
        p_content = block
        p_blocks = re.finditer(r'<p([^re]*?)</p>', block)
        for item in p_blocks:
            content = item.group()
            p_content = p_content.replace(content, parser_p(content))
        return p_content

    @staticmethod
    def __b_pip(self, block):
        block_content = block
        b_blocks = re.finditer(r'<b(.*?)</b>', block)
        for item in b_blocks:
            content = item.group()
            block_content = block_content.replace(content, parser_b(content))
        return block_content

    # 解析strong标签
    @staticmethod
    def __strong_pip(self, block):
        block_content = block
        strong_blocks = re.finditer(r'<strong(.*?)</strong>', block)
        for item in strong_blocks:
            content = item.group()
            block_content = block_content.replace(content, parser_strong(content))
        return block_content

    # 解析em 斜体标签
    @staticmethod
    def __em_pip(self, block):
        em_content = block
        em_blocks = re.finditer(r'<em(.*?)</em>', block)
        for item in em_blocks:
            content = item.group()
            em_content = em_content.replace(content, parser_em(content))
        return em_content

    # 解析img标签
    @staticmethod
    def __img_pip(self, block):
        img_content = block
        img_blocks = re.finditer(r'<img(.*?)>', block)
        for item in img_blocks:
            content = item.group()
            img_content = img_content.replace(content, parser_img(content))
        return img_content

    # 解析pre code标签
    @staticmethod
    def __pre_pip(self, block):
        pre_content = block
        pre_blocks = re.finditer(r'<pre(.*?)</pre>', block)
        for item in pre_blocks:
            content = item.group()
            pre_content = pre_content.replace(content, parser_pre(content))
        return pre_content

    # 解析code标签
    @staticmethod
    def __code_pip(self, block):
        code_content = block
        code_blocks = re.finditer(r'<code(.*?)</code>', block)
        for item in code_blocks:
            content = item.group()
            code_content = code_content.replace(content, parser_code(content))
        return code_content


# 解析 li 标签
# 可能还有其他子标签
# 需要首位的位置
def parser_li(block):
    return block


# 解析ul
def parser_ul(block):
    return parser_list(block)


# 解析ol
def parser_ol(block):
    return parser_list(block)


# 核心算法，解析列表标签
# 这个也是一个逆序算法，从后往前切割
# fix bug：2019年12月13日10:32:13 始终在后面，采用标记逆序奇偶互斥算法
# > 空格很多 <
def parser_list(block):
    # clear ul、ol tag
    block = re.sub(r'<ul(.*?)>', '<ul>', block)
    block = re.sub(r'<li(.*?)>', '<li>', block)
    block = remove_list_whitespace(block)  # 移除空格
    # 始终是一个干净的字符块，不做任何替换出来
    src_block = block
    content = block

    # storage variable
    ul_array = []
    ul_span = []
    left_ul_start = []
    right_ul_end = []
    left_ul_index = []
    right_ul_index = []
    left_ul_level = []
    # 存储li 所对应的的ul level 数组，然后取第一个，
    li_levels_map = {}  # [(index,(ul开始，li开始，ul结束,ul_level，ul_type))]
    ul_index_level = {}  # 索引值对应的level {0: 0, 1: 1, 2: 2, 5: 1, 3: 2, 4: 1, 6: 1, 7: 0}

    # get ul tag params
    def get_ul_tuple():
        for item in re.finditer(r'<ul>|</ul>|<ol>|</ol>', block):
            ul_array.append(item.group())
            if item.group() == '<ul>' or item.group() == '</ul>':
                ul_span.append(item.span() + ('ul',))
            elif item.group() == '<ol>' or item.group() == '</ol>':
                ul_span.append(item.span() + ('ol',))

    get_ul_tuple()

    # get left start tag <ul> <ol>
    def get_list_tag_name():
        for item in enumerate(ul_array):
            if item[1] == '<ul>' or item[1] == '<ol>':
                left_ul_start.append(item[1])
        for item in enumerate(ul_array):
            if item[1] == '</ul>' or item[1] == '</ol>':
                right_ul_end.append(item[1])

    get_list_tag_name()

    # get the tag index value
    def get_index():
        for item in enumerate(ul_array):
            if item[1] == '<ul>' or item[1] == '<ol>':
                left_ul_index.append(item[0])
        for item in enumerate(ul_array):
            if item[1] == '</ul>' or item[1] == '</ol>':
                right_ul_index.append(item[0])

    get_index()

    # 提取ul级别，核心算法一：提取<ul><ol>的level
    def get_level():
        for level in enumerate(left_ul_index):
            ul_index_level[level[1]] = level[0] * 2 - level[1]
            left_ul_level.append(level[0] * 2 - level[1])

    get_level()

    # 匹配对应的右边索引值
    right_ul_index = get_right_index(left_ul_index)

    # 组合索引值对应的map
    def get_li_level():
        # 为li 取得level
        li_block_list = re.finditer(r'<li>', src_block)
        for li_item in enumerate(li_block_list):
            li_index_key = li_item[0]
            value = li_item[1].span()
            li_start_key = value[0]
            for item in enumerate(left_ul_index):
                key = item[0]
                left_start_key = item[1]  # [0,1,2,4]  => [7,6,5,3]
                right_end_key = right_ul_index[key]  # [7,6,5,3]
                ul_start_key = ul_span[left_start_key][0]  # 0
                ul_end_key = ul_span[right_end_key][1]  # 1
                ul_the_level = left_ul_level[key]
                ul_the_type = ul_span[left_start_key][2]
                if ul_start_key < li_start_key < ul_end_key:
                    # (ul开始，li开始，ul结束,ul_level，ul_type)
                    tuple_params = (ul_start_key, li_start_key, ul_end_key, ul_the_level, ul_the_type)
                    li_levels_map[li_index_key] = tuple_params

    get_li_level()

    # 根据li_levels_map 去替换li 和计算ol>li的序列号
    for li in enumerate(re.finditer(r'<li>', src_block)):
        li_index = li[0]  # index
        li_value = li_levels_map[li_index]
        ul_start = li_value[0]
        li_start = li_value[1]
        ul_level = li_value[3]
        ul_type = li_value[4]
        if ul_type == 'ol':
            current_li_in_ol_index = src_block.count('<li>', ul_start, li_start)
            content = re.sub(r'<li>', ul_level * '    ' + str(current_li_in_ol_index) + '. ', content,
                             count=1)
            content = re.sub(r'</li>', '\n', content, count=1)
        if ul_type == 'ul':
            content = re.sub(r'<li>', '    ' * ul_level + '- ', content, count=1)
            content = re.sub(r'</li>', '\n', content, count=1)
        content = re.sub('<ul>|<ol>', '\n', content)
        content = re.sub('</ul>|</ol>', '', content)
    content = Pip(content).factory()
    return br_to_newline(content)


# 解析 pre code的标签，必须<pre><code>code</code></pre>
def parser_pre_block(block, language=""):
    clear_wrap_pre = remove_parent_wrap(block)
    if '<span' in clear_wrap_pre:
        span_elements = re.finditer(r'<span(.*?)</span>', clear_wrap_pre)
        for item in span_elements:
            span_string = item.group() or ""
            clear_wrap_pre = clear_wrap_pre.replace(span_string, get_tag_text(span_string))

    pre_content = clear_wrap_pre
    pre_content = parser_pre_code(pre_content)
    remove_nbsp_content = pre_content.replace('&nbsp;', ' ')
    remove_newline_content = br_to_newline(remove_nbsp_content)
    return '\n```' + language + '\n' + remove_newline_content + '\n```\n'


# bug  len(tuple(html_elements))会中断迭代循环
def parser_pre(element="", language=""):
    new_html = ""
    the_length = re.finditer(r'<pre(.*?)</pre>', element)
    length = len(list(the_length))
    if length > 1:
        raise RuntimeError('意外的数组长度：parser_pre', length)
    html_elements = re.finditer(r'<pre(.*?)</pre>', element)
    # 此时需要保证pre就一个标签
    for item in html_elements:
        block_string = item.group() or ""
        new_html = parser_pre_block(block_string, language=language)
        break
    return '\n' + new_html + '\n'


# 针对pre code
# code class="devsite-terminal" data-terminal-prefix=">>>" dir="ltr">x = tf.constant([1, 2, 3])</code>
def parser_pre_code(block):
    code_content = block
    code_blocks = re.finditer(r'<code(.*?)</code>', block)
    for item in code_blocks:
        content = item.group()
        code_content = code_content.replace(content, parser_code(content, code=""))
    return code_content


# h1-h6 可能还有其他子标签
def parser_head(block):
    text = block
    tag_name = get_tag_name(block)
    head = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
    if is_has_child(block):
        # 产生递归
        clear_content = clean_up(block)
        head_content = Pip(clear_content).factory()
        return parser_head(head_content)
    else:
        if tag_name in head:
            text = '\n\n' + '#' * int(tag_name[1]) + ' ' + get_tag_text(text) + '\n'
    return text


# 将code 解析为``,
# <code translate="no" dir="ltr">tf.compat.v2.clip_by_value</code>
# => tf.compat.v2.clip_by_value
# 存在一些属性例如：data-xx=">>>"的怪异属性
def parser_code(element="", whitespace=" ", code="`"):
    remove_attr_content = remove_attrs_value(element.strip())
    left = re.sub(r'<code(.*?)>', whitespace + code, remove_attr_content.strip())
    return re.sub(r'</code>', code + whitespace, left)


# 将a标签 <a href="/api_docs/python/tf/clip_by_value"><code translate="no" dir="ltr">tf.compat.v2.clip_by_value</code></a>
# 转为 [xx](xxx)

def parser_a(element=""):
    # 先检查a 标签里面包含其他东西
    the_href = get_href(element)
    left = re.sub(r'<a(.*?)>', '', element)
    a_content = re.sub(r'</a>', '', left)
    return '[' + check_what_element(element=a_content) + '](' + the_href + ')'


# 解析quote

def parser_quote(element=""):
    new_html = element
    html_blocks = re.finditer(r'<(.*?)(>)(.*?)(</(.*?)>)', new_html)
    for item in html_blocks:
        block_string = item.group() or ""
        new_html = new_html.replace(block_string, check_what_element(element=block_string))
    remove_parent = remove_parent_wrap(new_html)
    if 'blockquote' in remove_parent:
        remove_parent = remove_parent_wrap(remove_parent)
        return '\n> ' + Pip(remove_parent).factory() + '\n'
    return '\n> ' + Pip(remove_parent).factory() + '\n'


# 解析strong
def parser_strong(element=""):
    left = re.sub(r'<strong(.*?)>', '', element)
    strong_content = re.sub(r'</strong>', '', left)
    return '**' + check_what_element(element=strong_content).strip() + '** '


# 纯解析block 块
# <b>xxx</b>
def parser_b_block(block):
    left = re.sub(r'<b(.*?)>', '', block)
    b_content = re.sub(r'</b>', '', left)
    return '**' + get_tag_text(b_content).strip() + '** '


# 解析 b block
def parser_b(element=""):
    if is_has_child(element):
        remove_wrap = remove_parent_wrap(element)
        tag_name = get_tag_name(remove_wrap)
        if tag_name == 'code':
            return "**" + parser_code(remove_wrap, whitespace=" ").strip() + '** '
        else:
            return element
    return parser_b_block(element)


# 解析em 斜体
def parser_em(element):
    if is_has_child(element):
        remove_wrap = remove_parent_wrap(element)
        tag_name = get_tag_name(remove_wrap)
        if tag_name == 'em':
            return "*" + parser_code(remove_wrap, whitespace=" ").strip() + '* '
        else:
            return element
    return parser_em_block(element)


# 解析纯em斜体块
def parser_em_block(element):
    return '*' + remove_parent_wrap(element) + '*'


# 解析 img
def parser_img(block):
    src = get_src(block)
    alt = get_alt(block)
    return '![' + alt + '](' + src + ')'


# 解析 p块
def parser_p(block):
    block = remove_p(block)
    block = remove_span(block)
    block = check_what_element(element=block)
    block = br_to_empty(block)
    return block


# 解析，block，默认块
def parser_default(block):
    new_html = remove_parent_wrap(block)
    new_html = remove_span(new_html)
    ret = check_what_element(element=new_html)
    return '\n' + ret + '\n'


# 判断是哪种标签开头，但不完全是包围的
# 流水线处理
def check_what_element(element=""):
    clear_attrs_element = element
    # if not get_tag_name(element) == 'a':
    #     clear_attrs_element = remove_attrs(element)
    element = Pip(clear_attrs_element).factory()
    return element
