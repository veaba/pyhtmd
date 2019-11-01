import re


# 判断是否li开头的标签
def is_li(block):
    if re.match(r'^.*<li>', block):
        return True
    else:
        return False


# 判断是否是code标签

def is_code(block):
    if re.match(r'^.*<code>', block):
        return True
    else:
        return False


# 判断h1-h6

def is_head(block):
    if re.match(r'^.*\<([h1|h2|h3|h4|h5|h6])', block):
        return True
    else:
        return False


# 判断是image标签
def is_img(block):
    if re.match(r'^.*\<img', block):
        return True
    else:
        return False


# 判断是pre code 代码的标签
def is_pre(block):
    if re.match(r'^.*\<pre', block):
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
    return re.sub(r'<\/*\/([^\/]+[^\.])$', '', left)

# 移除换行符
def remove_new_line(block=""):
    return block.replace('\n','')
# 移除attrs
def remove_attrs(block):
    content=block
    remove_h1 = re.sub(r'<h1(.*?)">', '<h1>', content)
    remove_h2 = re.sub(r'<h2(.*?)">', '<h2>', remove_h1)
    remove_h3 = re.sub(r'<h3(.*?)">', '<h3>', remove_h2)
    remove_h4 = re.sub(r'<h4(.*?)">', '<h4>', remove_h3)
    remove_h5 = re.sub(r'<h5(.*?)">', '<h5>', remove_h4)
    remove_h6 = re.sub(r'<h6(.*?)">', '<h6>', remove_h5)
    remove_code = re.sub(r'<code(.*?)">', '<code>', remove_h6)
    remove_span = re.sub(r'<span(.*?)">', '<span>', remove_code)
    remove_button = re.sub(r'<button(.*?)">', '<button>', remove_span)
    remove_b = re.sub(r'<b(.*?)">', '<b>', remove_button)
    # 必须是button再导b标签
    # remove_b = re.sub(r'<button(.*?)">', '<button>', content) 正则替换引发：RecursionError: maximum recursion depth exceeded while calling a Python object
    remove_div = re.sub(r'<div(.*?)">', '<div>', remove_b)
    remove_a = re.sub(r'<a(.*?)">', '<a>', remove_div)
    return remove_a


# 移除父级标签直接获取内容
# <h1>xxx</h1> => xxx

def get_tag_text(block):
    text = ''
    if not is_has_child(block):
        text = remove_parent_wrap(block)
    else:
        return get_tag_text(remove_parent_wrap(block))
    return text


# 获取标签名，必须是干净标签，已移除attrs
# <code>xxx </code>
# ===> code
def get_tag_name(block):
    match_tag = re.match(r'<(.*?)>', block)
    return re.sub(r'<(.*?)>', '\\1', match_tag.group())
