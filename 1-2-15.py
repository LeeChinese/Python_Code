"""
演示Python的input语句
获取键盘的输入信息
"""
print("请告诉我你是谁？")
name = input()
print("我知道了，你是：%s" % name)

name = input("请告诉我你是谁：")  # input（）语句其实是可以在要求使用者输入内容前，输出提示的内容
print(type(name))
print("我知道了，你是：%s" % name)

# 输入数字类型
num = input("请告诉我你的银行卡密码：")
print("你的银行卡密码类型是：", type(num))  # input()语句不管你写入的是什么样的类型，都把它当作字符串来看待
# 数据类型转换
num = int(num)
print("你的银行卡密码类型是：", type(num))
