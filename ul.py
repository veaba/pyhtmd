import re

block = '<ul class="c545"><li class="dsad">111</li><li>222</li><li>333<ul><li>1111</li><li>2221</li><li>3333</li><li>4444</li></ul></li><li><ul><li>5555</li><li>6666</li><li>7777</li><li><ul><li>aaaa</li><li>bbbb</li><li>cccc</li><li>dddd</li></ul></li><ul><li>eeee</li><li>ffff</li><li>gggg</li><li>hhhh</li></ul></ul>444</li><ol><li>啊啊啊</li><li>哦哦哦</li></ol></ul>'

# 清空ul li attrs
block = re.sub(r'<ul(.*?)>', '<ul>', block)
block = re.sub(r'<li(.*?)>', '<li>', block)
# print('ret:', block)

# 获取在字符串中的索引值
ul_array = []
ul_span = []
left_ul_start = []
right_ul_end = []
left_ul_index = []
right_ul_index = []
left_ul_level = []
content = ''


def get_ul_tuple(init=False):
    if init:
        del ul_array[0:]
        del ul_span[0:]
    for item in re.finditer(r'<ul>|</ul>|<ol>|</ol>', block):
        ul_array.append(item.group())
        ul_span.append(item.span())
    # print('第1步-ul_span：', ul_span)
    # print('第1.1步-ul_array：', ul_array)


get_ul_tuple()


# 提取左边开始标签<ul <ol
def get_tag_name(init=False):
    if init:
        del left_ul_start[0:]
        del right_ul_end[0:]
    for item in enumerate(ul_array):
        if item[1] == '<ul>' or item[1] == '<ol>':
            left_ul_start.append(item[1])
    for item in enumerate(ul_array):
        if item[1] == '</ul>' or item[1] == '</ol>':
            right_ul_end.append(item[1])
    # print('第2步：', left_ul_start)  # ['<ul', '<ul', '<ul', '<ul', '<ul', '<ol']
    # print('第2.1步：', right_ul_end)  # ['</ul', '</ul', '</ul', '</ul', '</ol', '</ul']


get_tag_name()


# 提取索引值
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
    # print('第3-左边步：', left_ul_index)  # [0, 1, 3, 4, 6, 9]
    # print('第3.1-右边步：', right_ul_index)  # [2, 5, 7, 8, 10, 11]


get_index()
temp_right_ul_index_array = right_ul_index  # todo 用于计算右边索引值


# 提取ul级别，核心算法一：提取<ul><ol>的level

def get_level(init=False):
    if init:
        del left_ul_level[0:]
    for item in enumerate(left_ul_index):
        left_ul_level.append(item[0] * 2 - item[1] + 1)
    # print('第4步,获取level：', left_ul_level)


get_level()


def is_ul(string):
    if re.match(r'^<ul', string):
        return True
    else:
        return False


def is_ol(string):
    if re.match(r'^<ol', string):
        return True
    else:
        return False


# todo
def parser_ul(node, level):
    li_count = node.count('<li>')
    for index in range(li_count):
        node = re.sub(r'<li>', '    ' * level + '- ', node, count=1)
    node = re.sub(r'</li>', '\n', node)
    node = re.sub(r'<ul>', '', node)
    node = re.sub(r'</ul>', '', node)
    return node


# todo parser ol
def parser_ol(node, level):
    li_count = node.count('<li>')
    for index in range(li_count):
        node = re.sub(r'<li>', '    ' * level + str(index + 1) + '. ', node, count=1)
    node = re.sub(r'</li>', '\n', node)
    node = re.sub(r'<ol>', '', node)
    node = re.sub(r'</ol>', '', node)
    return node


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
    get_tag_name(init=True)
    get_index(init=True)
    get_level(init=True)

    # todo 解析ol
    if is_ol(current_node):
        content = content + parser_ol(current_node, current_level)

    # todo 解析ul
    if is_ul(current_node):
        content = parser_ul(current_node, current_level) + content

print(content)
