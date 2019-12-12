# 解析器
import re
# remove_attrs, \
from .utils import remove_parent_wrap, \
    remove_span, \
    br_to_newline, \
    br_to_empty, \
    remove_attrs_value, \
    remove_p, \
    is_has_child, \
    get_tag_text, \
    get_tag_name, \
    get_href, \
    get_src, get_alt, clean_up, \
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
        block_content = self.__code_pip(self, block_content)
        block_content = self.__em_pip(self, block_content)
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
        return block

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


# 纯ul标签
def parser_ul_block(node, level):
    for index in range(node.count('<li>')):
        node = re.sub(r'<li>', '    ' * level + '- ', node, count=1)
        node = remove_p(node)
    node = re.sub(r'</li>', '\n', node)
    node = re.sub(r'<ul>', '', node)
    node = re.sub(r'</ul>', '', node)
    return node


# 纯ol标签
def parser_ol_block(node, level):
    for index in range(node.count('<li>')):
        node = re.sub(r'<li>', '    ' * level + str(index + 1) + '. ', node, count=1)
        node = remove_p(node)
        # 移除p标签
    node = re.sub(r'</li>', '\n', node)
    node = re.sub(r'<ol>', '', node)
    node = re.sub(r'</ol>', '', node)
    return node


# 核心算法，解析列表标签
def parser_list(block):
    # clear ul、ol tag
    block = re.sub(r'<ul(.*?)>', '<ul>', block)
    block = re.sub(r'<li(.*?)>', '<li>', block)

    # storage variable
    ul_array = []
    ul_span = []
    left_ul_start = []
    right_ul_end = []
    left_ul_index = []
    right_ul_index = []
    left_ul_level = []
    content = ''

    # get ul tag params
    def get_ul_tuple(init=False):
        if init:
            del ul_array[0:]
            del ul_span[0:]
        for item in re.finditer(r'<ul>|</ul>|<ol>|</ol>', block):
            ul_array.append(item.group())
            ul_span.append(item.span())

    get_ul_tuple()

    # get left start tag <ul> <ol>
    def get_list_tag_name(init=False):
        if init:
            del left_ul_start[0:]
            del right_ul_end[0:]
        for item in enumerate(ul_array):
            if item[1] == '<ul>' or item[1] == '<ol>':
                left_ul_start.append(item[1])
        for item in enumerate(ul_array):
            if item[1] == '</ul>' or item[1] == '</ol>':
                right_ul_end.append(item[1])

    get_list_tag_name()

    # get the tag index value
    def get_index(init=False):
        if init:
            del left_ul_index[0:]
            del right_ul_index[0:]
        for item in enumerate(ul_array):
            if item[1] == '<ul>' or item[1] == '<ol>':
                left_ul_index.append(item[0])
        for item in enumerate(ul_array):
            if item[1] == '</ul>' or item[1] == '</ol>':
                right_ul_index.append(item[0])

    get_index()

    temp_right_ul_index_array = right_ul_index  # 用于计算右边索引值

    # 提取ul级别，核心算法一：提取<ul><ol>的level
    def get_level(init=False):
        if init:
            del left_ul_level[0:]
        for item in enumerate(left_ul_index):
            left_ul_level.append(item[0] * 2 - item[1])

    get_level()
    # 替换,此时left_ul_level和left_ul_index长度是一致的
    for i in range(len(left_ul_start) - 1, -1, -1):
        current_level = left_ul_level[i]
        left_index = left_ul_index[i]
        # 核心算法二：提取<ul><ol>对应</ul></ol>的索引值
        temp_right_array = [k for k in temp_right_ul_index_array if k > left_index]
        right_index = temp_right_array[0]
        temp_right_ul_index_array.remove(right_index)
        # 字符开始处
        start_index = ul_span[left_index][0]
        end_index = ul_span[right_index][1]
        # 当前节点的字符串
        current_node = block[start_index:end_index]
        block = block[0:start_index] + block[end_index:]
        get_ul_tuple(init=True)
        get_list_tag_name(init=True)
        get_index(init=True)
        get_level(init=True)

        # 解析ol
        if is_ol(current_node):
            content = content + parser_ol_block(current_node, current_level)

        # 解析ul
        if is_ul(current_node):
            content = parser_ul_block(current_node, current_level) + content

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


# h1-h6 todo 可能还有其他子标签
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
    html_blocks = re.finditer(r'<(.*?)(>)(.*?)(<\/(.*?)>)', new_html)
    for item in html_blocks:
        block_string = item.group() or ""
        new_html = new_html.replace(block_string, check_what_element(element=block_string))
    return '\n>' + remove_parent_wrap(new_html) + '\n'


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
