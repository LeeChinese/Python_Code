'''
演示案例：数一数有几个a
'''

# 定义字符串name
name = "itheima is a brand of itcast"
# 定义一个变量count计算有多少个a
count = 0

# for循环处理字符串
for x in name:
    if x == 'a':
        count += 1

print(f"字符串中有{count}个a")