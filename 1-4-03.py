"""
while循环猜数字案例
"""

# 获取范围1~100的随机数字
import random
num = random.randint(1, 100)

# 通过一个布尔类型的变量，做循环是否继续的标记
flag = True
# 定义一个变量记录一共猜测了多少次
count = 0

while flag:
    guess_num = int(input("输入你猜的数字："))
    count += 1
    if guess_num == num:
        print("猜中了")
        # 设置为False就是终止循环的条件
        flag = False
    else:
        if guess_num > num:
            print("你猜的大了")
        else:
            print("你猜的小了")
            
print(f"你一共猜了{count}次")