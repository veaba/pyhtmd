import re

HTML_TAGS = [
    '<a',
    '<b',
    '<button',
    '<div',
    '<h1',
    '<h2',
    '<h3',
    '<h4',
    '<h5',
    '<h6',
    '<img',
    '<pre',
    '<span',
]


# 判断是否li开头的标签
def is_li(block):
    if re.match(r'^<li', block):
        return True
    else:
        return False


# 判断是否是code标签,<code开头
def is_code(block):
    if re.match(r'^<code', block):
        return True
    else:
        return False


# 判断h1-h6

def is_head(block):
    if re.match(r'^<h([1-6])', block):
        return True
    else:
        return False


# 判断是image标签，即<img开头
def is_img(block):
    if re.match(r'^<img', block):
        return True
    else:
        return False


# 判断是pre code 代码的标签,pre开头
def is_pre(block):
    if re.match(r'^<pre', block):
        return True
    else:
        return False


# 判断是Quote，引用
def is_quote(block):
    if re.match(r'^<blockquote', block):
        return True
    else:
        return False


# 判断是content，不存在外边框了

def is_content(block):
    if get_tag_text(block) == block:
        return True
    else:
        return False


# 判断如果不是被包围的标签

def is_no_wrap(block):
    if re.match(r'^.*<(.*?)>.*$', block):
        return False
    else:
        return True


# todo 判断所包围的标签还含有子标签,
# 存在 True，不存在False

def is_has_child(block):
    first_remove = remove_parent_wrap(block)
    second_remove = remove_parent_wrap(first_remove)
    if first_remove == second_remove:
        return False
    else:
        return True
    # ***************************动作部分************************ #


# 获取href地址url
def get_href(block):
    the_href_element = re.search(r'(href=")(.+?)(")', block)
    if not the_href_element:
        return ""
    else:
        the_href = re.sub(r'(href=")(.+?)(")', '\\2', the_href_element.group())  # 获得a标签的地址
        return the_href


# 获取src地址url
def get_src(block):
    the_src_element = re.search(r'(src=")(.+?)(")', block)
    the_src = re.sub(r'(src=")(.+?)(")', '\\2', the_src_element.group())  # 获得a标签的地址
    return the_src


# 获取alt描述
def get_alt(block):
    the_alt_element = re.search(r'(alt=")(.+?)(")', block)
    group_text = ''
    if the_alt_element:
        group_text = the_alt_element.group()
    the_alt = re.sub(r'(alt=")(.+?)(")', '\\2', group_text)  # 获得a标签的地址
    return the_alt


# 清理span、button标签
def clean_up(block):
    clear_span = re.sub(r'(<span)(.*?)(<\/span>)', '\\2', block.strip())
    clear_button = re.sub(r'(<button)(.*?)(<\/button>)', '', clear_span.strip())
    return clear_button


# 剥离外边父级标签,等同于获取内容
def remove_parent_wrap(block):
    # todo
    left = re.sub(r'^<(.*?)(>)', '', block)
    right = re.sub(r'<\/*\/([^\/]+[^\.])$', '', left)
    return right


# 初始化标签
# 移除换行符
# 移除script标签
def init_html(block=""):
    # print('初始化入参：', block)
    block = block.replace('\n', '')
    block = re.sub(r'<script(.*?)</script>', '', block)
    block = re.sub(r'<math(.*?)</math>', '', block)
    block = re.sub(r'(<name(.*?)>)|(</name>)', '', block)  # 有些页面会出在<name>比如：https://tensorflow.google.cn/api_docs
    # /python/tf/DeviceSpec
    block = re.sub(r'(<id(.*?)>)|(</id>)', '', block)
    block = re.sub(r'(<device_type(.*?)>)|(</device_type>)', '', block)
    block = re.sub(r'(<devsite-code(.*?)>)|(</devsite-code>)', '', block)
    # 转换特殊字符,todo，后续可能有其他特殊字符，这里需要继续补充
    block = block.replace('&gt;', '>')
    block = block.replace('&lt;', '<')
    # print('初始化结果:', block)
    return block


# 移除br
def remove_br(block):
    return block.replace('<br>', '\n').replace('</br>', '\n').replace('    ', '\n    ')


# 移除attrs
def remove_attrs(block):
    # print('移除attrs入参：', block)
    content = block
    normal_tags = []  # 如果是空数组，则原样返回
    for item in HTML_TAGS:
        if item in block:
            normal_tags.append(item)
    if not len(normal_tags):
        return content
    remove_h1 = re.sub(r'<h1(.*?)">', '<h1>', content)
    remove_h2 = re.sub(r'<h2(.*?)">', '<h2>', remove_h1)
    remove_h3 = re.sub(r'<h3(.*?)">', '<h3>', remove_h2)
    remove_h4 = re.sub(r'<h4(.*?)">', '<h4>', remove_h3)
    remove_h5 = re.sub(r'<h5(.*?)">', '<h5>', remove_h4)
    remove_h6 = re.sub(r'<h6(.*?)">', '<h6>', remove_h5)
    remove_pre = re.sub(r'<pre(.*?)">', '<pre>', remove_h6)
    remove_code = re.sub(r'<code(.*?)">', '<code>', remove_pre)
    remove_span_attr = re.sub(r'<span(.*?)">', '<span>', remove_code)
    remove_button = re.sub(r'<button(.*?)">', '<button>', remove_span_attr)
    remove_a = remove_button
    remove_a_attrs = re.search(r'<a(.*?)></a>', remove_button)
    if remove_a_attrs:
        remove_a_attrs_text = remove_a_attrs.group()
        if not is_has_child(remove_a_attrs_text):
            remove_a = re.sub(r'<a(.*?)></a>', '', remove_button)  # 需要保留src 和href 属性
        else:
            return remove_button
    print('remove_a:', remove_a)
    remove_b = re.sub(r'<b(.*?)">', '<b>', remove_a)
    remove_div = re.sub(r'<div(.*?)">', '<div>', remove_b)
    # 移除标签，如果内容不存在的话移除,针对无意义button、a标签。比如<h2>Modules<button></button><a></a></h2>  => <h2>Modules</h2>
    ret = re.sub(r'(<button></button>|<a></a>)', '', remove_div)
    # print('移除attrs结果：', ret)
    return ret


# 移除span标签
def remove_span(block):
    return re.sub(r'(<span(.*?)>)|(</span>)', '', block)


# 移除标签
def remove_p(block):
    return re.sub(r'(<p(.*?)>)|(</p>)', '', block)


# 移除父级标签直接获取内容
# <h1>xxx</h1> => xxx

def get_tag_text(block):
    block = remove_br(block)
    print('获取内容，get_tag_text:\n', block)
    if is_has_child(block):
        return get_tag_text(remove_parent_wrap(block))
    return block


# 获取标签名，必须是干净标签，已移除attrs
# <code>xxx </code>  ===》 code
# <a href="https://baidu.com">baidu.com </a>  ===> a
# <h2>Class <code>DeviceSpec</code></h2>

def get_tag_name(block):
    print('获得标签名入参：', block)
    match_tag = re.match(r'<(.*?)>', block)
    if match_tag:
        # 如果存在 类似 <a href="https://baidu.com">
        tag_string = match_tag.group()
        # 存在空格
        if ' ' in tag_string:
            exist_tag = re.sub(r'<(.*?) .*$', '\\1', tag_string)
            print('获得标签名出参：', exist_tag)
            return exist_tag
    last_tag_name = re.sub(r'<(.*?)>.*$', '\\1', block, count=1)
    print("获得标签名出参：", last_tag_name)
    return last_tag_name
