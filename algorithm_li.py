# 解析html ul 算法
# 指定任意ul，获取它的level
ul ='[[][[]][[[[]]]][]]'
left_index_array=[] # [0, 1, 3, 4, 7, 8, 9, 10, 15]
left_level_array=[] # 

# 提取[ 索引值
for item in enumerate(ul):
    k=item[0]
    v=item[1]
    if v=='[':
        left_index_array.append(k)
# 



x =[i for i in ul if i=='['] #['[', '[', '[', '[', '[', '[', '[', '[', '[']

for item in enumerate(left_index_array):
    k=item[0]
    v=left_index_array[k]
    left_level_array.append(2*k-v+1) # 核心算法

print('所对应Index：',left_index_array)
print('所对应Level：',left_level_array)

