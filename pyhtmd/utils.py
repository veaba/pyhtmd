import re

HTML_TAGS = [
    '<a',
    '<b',
    '<button',
    '<ul',
    '<ol',
    '<li',
    '<div',
    '<h1',
    '<h2',
    '<h3',
    '<h4',
    '<h5',
    '<h6',
    '<img',
    '<p',
    '<pre',
    '<span',
]


# 比如 <img <br 等不需要关闭的标签
def is_no_close_tag(block):
    if re.match(r'^(<img)|(<br)+(.*?)>$', block):
        return True
    else:
        return False


# 判断是自定义node
def is_custom_node(block):
    if re.match(r'^<+(.*?)>+$', block):
        if not is_no_close_tag(block) and not is_html_node(block):
            return True
        else:
            return False
    else:
        return False


# 判断是节点<a>x</a><img> <br>
def is_html_node(block):
    front_6_str = block[0:6]
    _is_node = False
    for tag in HTML_TAGS:
        if re.match(r'^' + tag + '', front_6_str):
            _is_node = True
            break
    return _is_node


# 判断是否li开头的标签
def is_li(block):
    if re.match(r'^<li', block):
        return True
    else:
        return False


def is_p(block):
    if re.match(r'(^<p>)|(^<p )(.*?)>$', block):
        return True
    else:
        return False


# 判断ul开头标签
def is_ul(block):
    if re.match(r'^<ul', block):
        return True
    else:
        return False


# 判断ol开头标签
def is_ol(block):
    if re.match(r'^<ol', block):
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


# 判断是em斜体
def is_em(block):
    if re.match(r'^<em', block):
        return True
    else:
        return False


# 判断所包围的标签还含有子标签,
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
    clear_span = re.sub(r'(<span)(.*?)(</span>)', '\\2', block.strip())
    clear_button = re.sub(r'(<button)(.*?)(</button>)', '', clear_span.strip())
    return clear_button


# 剥离外边父级标签,等同于获取内容
def remove_parent_wrap(block):
    left = re.sub(r'^<(.*?)[^=]>|^<(.*?)>', '', block)
    right = re.sub(r'</*/([^/]+[^.])$', '', left)
    return right


# 移除 list标签之间的空格
def remove_list_whitespace(block):
    content = block
    list_array = re.findall(r'(ul>|</ul>|li>|<li>|ol>|</ol>)(.*?)(<li|</li|</ul>|</ol>)', block)
    for items in list_array:
        for item in items:
            if not len(item.strip()):
                content = block.replace(item, '')
    return content


# 获取list将
# 过滤字符，只剩下<ul></ul><ol></ol>
def get_li_wrap(block):
    return block


# 初始化标签
# 移除换行符
# 移除script标签
def init_html(block=""):
    block = block.strip()
    block = re.sub(r'(\n$)|(^\n)|(\n\n)|(\n)', '', block)
    block = re.sub(r'<script(.*?)</script>', '', block)
    block = re.sub(r'<math(.*?)</math>', '', block)
    block = re.sub(r'(<name(.*?)>)|(</name>)', '', block)  # 有些页面会出在<name>比如：https://tensorflow.google.cn/api_docs

    # 移除无关自定义标签,比如一些乱七八糟的自定义tag
    # 如果不属于HTML_TAGS 则移除他的外边框
    if is_custom_node(block):
        block = remove_parent_wrap(block)
    # /python/tf/DeviceSpec
    block = re.sub(r'(<id(.*?)>)|(</id>)', '', block)
    block = remove_button(block)
    block = remove_span(block)
    block = remove_div(block)
    # 转换特殊字符,后续可能有其他特殊字符，这里需要继续补充
    block = block.replace('&gt;', '>')
    block = block.replace('&lt;', '<')
    return block


# 警告：移除自定义标签，这个方法会稍显危险，会移除所有不认识的标签，HTML_TAGS
def remove_custom(block):
    tag_start_end_list = re.findall(r'<(.*?)>', block)
    content = block
    for tag in tag_start_end_list:
        if '<' + tag not in HTML_TAGS:
            content = re.sub(r'' + '<' + tag + '(.*>)|</' + tag + '>', '', content)
    return content


# 移除br
def remove_br(block):
    return block.replace('<br>', '\n').replace('</br>', '\n').replace('    ', '\n    ')


# 移除attrs，不限制任何标签
def remove_attrs_value(block):
    return re.sub(r' (.*?)="(.*?)"', '', block)


# 移除attrs
def remove_attrs(block):
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
    remove_button_attr = re.sub(r'<button(.*?)">', '<button>', remove_span_attr)
    remove_a = remove_button_attr
    remove_a_attrs = re.search(r'<a(.*?)></a>', remove_button_attr)
    if remove_a_attrs:
        remove_a_attrs_text = remove_a_attrs.group()
        if not is_has_child(remove_a_attrs_text):
            remove_a = re.sub(r'<a(.*?)></a>', '', remove_button_attr)  # 需要保留src 和href 属性
        else:
            return remove_button
    remove_b = re.sub(r'<b(.*?)">', '<b>', remove_a)
    remove_div_attr = re.sub(r'<div(.*?)">', '<div>', remove_b)
    # 移除标签，如果内容不存在的话移除,针对无意义button、a标签。比如<h2>Modules<button></button><a></a></h2>  => <h2>Modules</h2>
    ret = re.sub(r'(<button></button>|<a></a>)', '', remove_div_attr)
    return ret


# br转\n
def br_to_newline(block):
    return block.replace('<br>', '\n')


# br 清除
def br_to_empty(block):
    return block.replace('<br>', '')


# 移除span标签
def remove_span(block):
    return re.sub(r'(<span(.*?)>)|(</span>)', '', block)


# 移除p标签,希望是不误杀<pre>标签
def remove_p(block):
    block = re.sub(r'<p([^re]*?)>', '', block)
    return re.sub(r'</p>', '\n\n', block)


# 移除button
def remove_button(block):
    return re.sub(r'(<button(.*?)>)|(</button>)', '', block)


# 移除div
def remove_div(block):
    return re.sub(r'(<div(.*?)>)|(</div>)', '', block)


# 移除nbsp
def remove_nbsp(block):
    return re.sub(r'&nbsp;|&nbsp; ', ' ', block)


# 移除父级标签直接获取内容
# <h1>xxx</h1> => xxx
def get_tag_text(block):
    block = remove_br(block)
    if is_has_child(block):
        return get_tag_text(remove_parent_wrap(block))
    return remove_parent_wrap(block)


# 获取标签名，必须是干净标签，已移除attrs
# <code>xxx </code>                             ===> code
# <a href="https://baidu.com">baidu.com </a>    ===> a
# <h2>Class <code>DeviceSpec</code></h2>
# daddd                                         ===> daddd
# a                                             ===> a
def get_tag_name(block):
    match_tag = re.match(r'<(.*?)>', block)
    if match_tag:
        # 如果存在 类似 <a href="https://baidu.com">
        tag_string = match_tag.group()
        # 存在空格
        if ' ' in tag_string:
            exist_tag = re.sub(r'<(.*?) .*$', '\\1', tag_string, count=1)
            return exist_tag
    last_tag_name = re.sub(r'<(.*?)>.*$', '\\1', block, count=1)
    return last_tag_name


# **** level 标记逆序奇偶互斥算法（帅气的名字）*********

# 是偶数则返回True，否则返回False
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


# @desc 根据入参left 获取对应right 的数组
# @具体算法见https://github.com/veaba/learn-python/
def get_right_index(left):
    left_count = len(left)
    all_array = [i for i in range(left_count * 2)]
    right_array_temp = list(set(all_array).difference(set(left)))
    right_array = []
    all_len = len(all_array)
    max_value = all_len - 1
    left_len_value = len(left)

    for i in range(left_len_value - 1, -1, -1):
        k = i
        v = left[i]
        if k == left_len_value - 1:
            right_array.insert(0, v + 1)
        elif k == 0:
            right_array.insert(0, max_value)
        else:
            right_stay_array = list(set(right_array_temp).difference(set(right_array)))  # 取临时数组和right_array的交集
            big_then_array = [big for big in right_stay_array if big > v]  # 取出比v还大的数组
            if is_even(v):
                mutex_array = [mutex for mutex in big_then_array if not is_even(mutex)]  # 当v为偶数时候，取出奇数
            else:
                mutex_array = [mutex for mutex in big_then_array if is_even(mutex)]  # 当v为奇数时候，取出偶数
            min_value = min(mutex_array)
            right_array.insert(0, min_value)

    return right_array
