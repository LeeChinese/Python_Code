"""
练习案例：
猜猜心里数字
"""

# 定义一个变量数字
num = int(input("请输入你想的数字："))

# 通过键盘输入获取猜想的数字，通过if多条件判断进行猜想比较
if int(input("输入第一次你猜的数字：")) == num:
    print("你猜对了")
elif int(input("不对，再猜一次：")) == num:
    print("你猜对了")
elif int(input("不对，再猜最后一次：")) == num:
    print("你猜对了")
else:
    print("Sorry，全部猜错了，我想的是：%d" % num)