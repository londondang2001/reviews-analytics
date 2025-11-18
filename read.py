# 1. 读取留言档
# 2. 测试印出data清单
# 3. 只印出第0笔
# 4. 读取档案的过程中, 印出len(data)得知读取进度, 总共有多少留言
# 5. 算留言平均长度

data = [] 
count = 0
with open('reviews.txt', 'r') as f:
	for line in f: 
		data.append(line.strip()) 
		count += 1
		if count % 10000 == 0:  # 如果count是1000的倍数, 就可以被1000整除
			print(len(data)) # 每读1000行, 印一次清单长度
print('档案读取完了, 总共有', len(data), '笔资料')

sum_len = 0 
for d in data:  # 对每一笔留言计算长度
	sum_len = sum_len + len(d) 
print('留言的平均长度为', sum_len / len(data))

new = []
for d in data:
	if len(d) < 100:  # 筛选长度小于100的留言
		new.append(d)
print('一共有', len(new), '笔留言长度小于100')

good = []
for d in data:
	if 'good' in d:
		good.append(d)  # 一般原封不动地加入清单, 用于计算留言笔数, 也可加1, True, 或增加一段字符
print('一共有', len(good), '笔留言中提到good')

# 速写法, output = [(number-1) for number in reference if number % 2 == 0]
# good = [1 for d in data if 'good' in d]
# print(good)

# bad = ['bad' in d for d in data ]
# print(bad)

# 100万笔的留言中, 每一个字出现几次, 哪个字最常出现
# 字典关键用法, 检查某个字是否出现在字典里, 如果你没有出现过, 就化为1, 如果出现过, 就把现在的值给加1, 将每个字都存入字典, 对应一个值, words ['These'] = 'count' 

# 计算每个字出现的次数

wc = {}
for d in data:                            # 从清单读取每一个字段
	words = d.split()                     # 从字段的空格切出每一个词
	for word in words:                    # 从很多个词中读取每一个词
		if word in wc:                    # 问是否出现过, 如果字在wc字典出现过
			wc[word] = wc[word] + 1       # 设定新的value
		else:                             # 如果没有出现过
			wc[word] = 1                  # 新增新的key进wc字典, value为1
# print(wc)
# 用 for loop 印字典

for word in wc:                  # 从字典中读取每一个钥匙
	if wc[word] > 1000000:       # 从字典中查找钥匙, 如果值大于100
		print(word, wc[word])    # 印出钥匙和配对值

print(len(wc))                   # 字典的长度, 总共有多少钥匙

# 让使用者查字

print(wc['William'])
while True:
	word = input('请输入你想查什么字:')
	if word == 'q':
		break	
	if word in wc:               # 如果word在wc字典里
		print(word, '出现过的次数为: ', wc[word])
	else:                        # 如果不在
		print('这个字没有出现过')
print('感谢使用本查询功能')

# 避免当掉