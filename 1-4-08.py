'''
range语句：
语法1：range（num） 获取一个从0开始，到num结束的数字序列（不包含num本身）
语法2：range（num1， num2） 获取一个从num1开始，到num2结束的数字序列（不包含num2本身）
语法3：range（num1， num2， step） 获得一个从num1开始，到num2结束的数字系列（不含num2本身）
数字之间的步长，以step为准（step默认为1）
如，range（5， 10， 2）取得的数据是：[5, 7, 9] 
'''

# range语法1 range（num）
for x in range(10):
    print(x)

# range语法2 range（num1， num2）
for x in range(5, 10):
    # 从5开始，到10结束（不包含10本身）的一个数字序列，数字之间的间隔是1
    print(x)

# range语法3 range（num1， num2，step）
for x in range(5, 10, 2):
    # 从5开始，到10结束（不包含10本身）的一个数字序列，数字之间的间隔是2
    print(x)
for x in range(10):
    print("送玫瑰花")


"""
练习案例：
有几个偶数
"""

# 通过键盘输入数字
num = int(input("请输入数字序列的最大值"))
# 定义变量记录偶数的数量
count = 0

# 通过for循环和if判断语句处理
for x in range(1, num):
    if x % 2 == 0:
        count += 1

print(count)