# 1. 读取留言档
# 2. 测试印出data清单
# 3. 只印出第0笔
# 4. 读取档案的过程中, 印出len(data)得知读取进度
# 5. 算留言平均长度

data = [] # 空清单
count = 0
with open('reviews.txt', 'r') as f:
	for line in f: # 读取数据档的每一行,一行一行地取值
		data.append(line.strip()) # 把每一行装进data清单里 
		count += 1
		if count % 1000 == 0:  # 如果count是1000的倍数, 就可以被1000整除
			print(len(data)) 
                         # 每读1000行, 印一次data清单长度
                         # 通过计数, 记录循环次数, 知道读取进程状态
print(len(data))
print(data[0])
print('---------------')
print(data[1])


