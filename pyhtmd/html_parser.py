# 解析器
import re
from .utils import remove_parent_wrap, \
remove_attrs,  \
is_has_child,  \
get_tag_text, \
get_tag_name,  \
get_href,\
get_src,get_alt, clean_up
# ***************************解析部分************************ #
# 将获取被包围的node节点解析成为数组
# Given a tensor <code translate="no" dir="ltr">t<\/code>, this operation returns a tensor of the same type  andshape as <code translate="no" dir="ltr">t<\/code> with its values clipped to <code translate="no"
# dir="ltr">clip_value_min<\/code> and <code translate="no" dir="ltr">clip_value_max</code>.Any values less than
# <code translate="no" parser_bdir="ltr">clip_value_min</code> are set to <code translate="no"
# dir="ltr">clip_value_min</code>. Any valuesgreater than <code translate="no" dir="ltr">clip_value_max</code> are
# set to <code translate="no" dir="ltr">clip_value_max</code>.
# ===> re.finditer(r'<(.*?)(>)(.*?)(<\/(.*?)>)', h)
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
        block_content = self.__a_pip(self.block)
        block_content = self.__p_pip(block_content)
        block_content = self.__b_pip(self, block_content)
        block_content = self.__strong_pip(block_content)
        block_content = self.__code_pip(block_content)
        return block_content

    def __a_pip(self, block):
        block_content=block
        a_blocks=re.finditer(r'<a(.*?)</a>', block)
        for item in a_blocks:
            content=item.group()
            block_content=block_content.replace(content,parser_a(content))
        return block_content


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

    def __strong_pip(self, block):
        block_content = block
        strong_blocks = re.finditer(r'<strong(.*?)</strong>', block)
        for item in strong_blocks:
            content = item.group()
            block_content = block_content.replace(content, parser_strong(content))
        return block_content

    def __code_pip(self, block):
        code_content=block
        code_blocks = re.finditer(r'<code(.*?)</code>', block)
        # todo 先处理b标签
        for item in code_blocks:
            content=item.group()
            code_content=code_content.replace(content,parser_code(content))
        return code_content


# 解析 li 标签
# todo 可能还有其他子标签
def parser_li(block):
    temp_array = re.finditer(r'\<li\>(.*?)\<\/li\>', block)
    text = ''
    for ele in temp_array:
        # 判断不存在包围子元素
        if not is_has_child(ele.group()):
            text = '\n- '+get_tag_text(block)
        # 如果存在子元素
        else:
            remove_li_tag = remove_parent_wrap(ele.group())
            text += '\n- ' + check_what_element(element=remove_li_tag) + '\n'
    return text


# 解析 pre code的标签
def parser_pre(block):
    content = get_tag_text(block).replace('    ', '\n')
    content_remove_code = get_tag_text(content)
    return '\n```\n' + content_remove_code + '\n```\n'

# h1-h6 todo 可能还有其他子标签
def parser_head(block):
    text = block
    tag_name = get_tag_name(block)
    if is_has_child(block):
        clearn_content = clean_up(block)
        return parser_head(clearn_content)
    else:
        if tag_name == 'h1':
            text = '\n# ' + get_tag_text(text) + '\n'
        elif tag_name == 'h2':
            text = '\n## ' + get_tag_text(text) + '\n'
        elif tag_name == 'h3':
            text = '\n### ' + get_tag_text(text) + '\n'
        elif tag_name == 'h4':
            text = '\n#### ' + get_tag_text(text) + '\n'
        elif tag_name == 'h5':
            text = '\n##### ' + get_tag_text(text) + '\n'
        elif tag_name == 'h6':
            text = '\n###### ' + get_tag_text(text) + '\n'
    return text


# 将code 解析为``,
# <code translate="no" dir="ltr">tf.compat.v2.clip_by_value</code>
# => tf.compat.v2.clip_by_value

def parser_code(element="",whitespace=""):
    left = re.sub(r'<code(.*?)>', whitespace+'`', element.strip())
    return re.sub(r'</code>', '`'+whitespace, left)


# 将a标签 <a href="/api_docs/python/tf/clip_by_value"><code translate="no" dir="ltr">tf.compat.v2.clip_by_value</code></a>
# 转为 [xx](xxx)

def parser_a(element=""):
    # todo 先检查a 标签里面包含其他东西
    the_href = get_href(element)
    left = re.sub(r'<a(.*?)>', '', element)
    a_content = re.sub(r'</a>', '', left)
    return '[' + check_what_element(element=a_content) + '](' + the_href + ')'


# 解析strong
def parser_strong(element=""):
    left = re.sub(r'<strong(.*?)>', '', element)
    strong_content = re.sub(r'</strong>', '', left)
    return '**' + check_what_element(element=strong_content) + '**'


# 纯解析block 块
def parser_b_block(block):
    left = re.sub(r'<b(.*?)>', '', block)
    b_content = re.sub(r'</b>', '', left)
    return '**' + get_tag_text(b_content) + '**'

# 解析 b block
def parser_b(element=""):
    if is_has_child(element):
        remove_wrap= remove_parent_wrap(element)
        tag_name=get_tag_name(remove_wrap)
        if tag_name =='code':
            return "**"+parser_code(remove_wrap,whitespace=" ")+'**'
        else:
            raise RuntimeError('意外的类型，需要调整源码')
    return parser_b_block(element)

# 解析 img

def parser_img(block):
    src=get_src(block)
    alt=get_alt(block)
    return '!['+alt+']('+src+')'

# 解析，p block，默认块
def parser_p(block):
    new_html=block
    html_blocks = re.finditer(r'<(.*?)(>)(.*?)(<\/(.*?)>)', new_html)
    for item in html_blocks:
        block_string = item.group() or ""
        new_html = new_html.replace(block_string, check_what_element(element=block_string))
    return '\n'+new_html+'\n'


# 判断是哪种标签开头，但不完全是包围的，todo，此时先判断code
# todo 流水线处理
def check_what_element(element=""):
    clear_attrs_element = remove_attrs(element)
    element=Pip(clear_attrs_element).factory()
    return element

