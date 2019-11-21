import re
block='<ul class="c545"><li class="dsad">111</li><li>222</li><li>333<ul><li>1111</li><li>2221</li><li>3333</li><li>4444</li></ul></li><li><ul><li>5555</li><li>6666</li><li>7777</li><li><ul><li>aaaa</li><li>bbbb</li><li>cccc</li><li>dddd</li></ul></li><ul><li>eeee</li><li>ffff</li><li>gggg</li><li>hhhh</li></ul></ul>444</li><ol><li>啊啊啊</li><li>哦哦哦</li></ol></ul>'


ul_array=re.findall(r'<ul|</ul|<ol|</ol',block)
# ul_array=[ul+'>' for ul in ul_array]
print('第一步：',ul_array)


# 提取左边开始标签<ul <ol
left_ul_start=[item[1] for item in enumerate(ul_array) if item[1]=='<ul' or item[1]=='<ol']
print('第二步：',left_ul_start) # [0, 1, 3, 4, 6, 9]
# 提取索引值
left_ul_index=[item[0] for item in enumerate(ul_array) if item[1]=='<ul' or item[1]=='<ol']
print('第三步：',left_ul_index) # [0, 1, 3, 4, 6, 9]

# 提取ul级别
left_ul_level=[item[0]*2-item[1]+1 for item in enumerate(left_ul_index)]
print('第四步：',left_ul_level) # [1, 2, 2, 3, 3, 2]

# 替换,此时left_ul_level和left_ul_index长度是一致的

for item in enumerate(left_ul_start):
    index=item[0]
    value=item[1]
    block=re.sub(r''+value+'(.*?)>','\n'+('  '*left_ul_level[index]),block)
print('第五步：',block)


# a="""
# <ul class="c545"><li class="dsad">111</li><li>222</li><li>333<ul><li>1111</li><li>2221</li><li>3333</li><li>4444</li></ul></li><li><ul><li>5555</li><li>6666</li><li>7777</li><li><ul><li>aaaa</li><li>bbbb</li><li>cccc</li><li>dddd</li></ul></li><ul><li>eeee</li><li>ffff</li><li>gggg</li><li>hhhh</li></ul></ul>444</li><ol><li>啊啊啊</li><li>哦哦哦</li></ol></ul>

# """

# b=re.sub(r'<ul(.*?)>(.*?)<li(.*?)>','\n - ',a)
# print(b)
# b=re.sub(r'</li>','',b)
# print(b)