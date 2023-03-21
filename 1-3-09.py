"""
演示判断判断语句的实战案例，终极猜数字
"""

# 1. 构建一个随机的数字变量
import random
num = random.randint(1, 10)

guess_num = int(input("输入你猜测的数字："))

# 2、通过if判断语句进行判断猜测
if guess_num == num:
    print("恭喜你，第一次就猜中了")
else:
    if guess_num > num:
        print("big")
    else:
        print("small")

    guess_num = int(input("输入你猜测的数字："))

    if guess_num == num:
        print("恭喜你，第二次就猜中了")
    else:
        if guess_num > num:
            print("big")
        else:
            print("small")

        guess_num = int(input("输入你猜的数字："))

        if guess_num == num:
            print("恭喜你，第三次就猜中了")
        else:
            print("三次机会都没有猜中")