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
		if count % 10000 == 0:  # 如果count是1000的倍数, 就可以被1000整除
			print(len(data)) 
                         # 每读1000行, 印一次data清单长度
                         # 通过计数, 记录循环次数, 知道读取进程状态
print('档案读取完了, 总共有', len(data), '笔资料')

sum_len = 0 # 加总
for d in data:
	sum_len = sum_len + len(d) # 加上每一笔留言的长度
	                           # 跟目前的总数加在一起, 存回总数
print('留言的平均长度为', sum_len / len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)

print('一共有', len(new), '笔留言长度小于100')


