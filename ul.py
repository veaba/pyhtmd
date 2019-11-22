import re

block = '<ul class="c545"><li class="dsad">111</li><li>222</li><li>333<ul><li>1111</li><li>2221</li><li>3333</li><li>4444</li></ul></li><li><ul><li>5555</li><li>6666</li><li>7777</li><li><ul><li>aaaa</li><li>bbbb</li><li>cccc</li><li>dddd</li></ul></li><ul><li>eeee</li><li>ffff</li><li>gggg</li><li>hhhh</li></ul></ul>444</li><ol><li>啊啊啊</li><li>哦哦哦</li></ol></ul>'

ul_array_iter = re.finditer(r'<ul|</ul|<ol|</ol', block)

# 获取在字符串中的索引值
ul_array = []
ul_span = []
for item in ul_array_iter:
    # 获取  ['<ul', '<ul', '</ul', '<ul', '<ul', '</ul', '<ul', '</ul', '</ul', '<ol', '</ol', '</ul']
    ul_array.append(item.group())
    ul_span.append(item.span())

# ul_array = re.findall(r'<ul|</ul|<ol|</ol', block)
# ul_array=[ul+'>' for ul in ul_array]
print('第1步：', ul_span)
print('第1.1步：', ul_array)

# 提取左边开始标签<ul <ol
left_ul_start = [item[1] for item in enumerate(ul_array) if item[1] == '<ul' or item[1] == '<ol']
right_ul_end = [item[1] for item in enumerate(ul_array) if item[1] == '</ul' or item[1] == '</ol']
print('第2步：', left_ul_start)   # ['<ul', '<ul', '<ul', '<ul', '<ul', '<ol']
print('第2.1步：', right_ul_end)  # ['</ul', '</ul', '</ul', '</ul', '</ol', '</ul']
# 提取索引值
left_ul_index = [item[0] for item in enumerate(ul_array) if item[1] == '<ul' or item[1] == '<ol']
right_ul_index = [item[0] for item in enumerate(ul_array) if item[1] == '</ul' or item[1] == '</ol']
print('第3步：', left_ul_index)  # [0, 1, 3, 4, 6, 9]
print('第3.1步：', right_ul_index)  # [0, 1, 3, 4, 6, 9]

# 提取ul级别
left_ul_level = [item[0] * 2 - item[1] + 1 for item in enumerate(left_ul_index)]
print('第4步：', left_ul_level)  # [1, 2, 2, 3, 3, 2]

# 替换,此时left_ul_level和left_ul_index长度是一致的

# 清空ul li attrs
block = re.sub(r'<ul(.*?)>', '<ul>', block)
block = re.sub(r'<li(.*?)>', '<li>', block)
print('ret:', block)

for i in range(len(left_ul_start) - 1, -1, -1):
    print('left-倒序后的标签名：', left_ul_start[i])
    print('left-倒序后的标签名索引：', left_ul_index[i])
    print('right-倒序后的标签名索引：', right_ul_index[i])
    start_index = ul_span[left_ul_index[i]][0]
    end_index = ul_span[right_ul_index[i]][1]
    print('字符的开始处：', start_index, end_index)
    print('截取的字符串：', block[start_index:end_index])
    # temp_split_str =
