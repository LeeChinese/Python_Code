'''
演示:快速体验函数的开发及应用
'''
# 需求:统计字符串的长度,不适用内置函数len()

str1 = "itheima"
str2 = "nihao"
str3 = "hello world"


# 使用函数,来优化这个过程
def my_len(data):
    count = 0
    for i in data:
        count += 1
    print(f"字符串{data}的长度是{count}")


my_len(str1)
my_len(str2)
my_len(str3)