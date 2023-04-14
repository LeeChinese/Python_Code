"""
演示函数综合案例开发
"""

# 定义两个全局变量money和name
money = 5000000
name = None
# 要求客户输入姓名
name = input("请输入您的姓名：")


# 定义查询余额函数
def query(show_header):
    if show_header:
        print("-----------查询余额----------")
    print(f"{name}，您好，您的余额剩余：{money}元")


# 定义存款效果函数
def deposit(num):
    print("------------存款-------------")
    global money  # money在函数内部定义全局变量
    money += num
    print(f"{name}，您好，您存款{num}元成功")
    # 调用query函数查询余额
    query(False)


# 定义取款效果函数
def withdrawal(num):
    print("------------取款-------------")
    global money  # 在函数内部定义全局变量
    money -= num
    print(f"{name}，您好，您取款{num}元成功")
    # 调用query函数查询余额
    query(False)


# 定义主菜单函数
def main_menu():
    print("------------主菜单-----------")
    print(f"{name}，您好，欢迎来到黑马银行ATM，请选择操作：")
    print("查询余额\t[输入1]")  # 通过\t制表符对齐输出
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return input("请输入您的选择：")


# 设置无限循环，确保程序不会退出
while True:
    keyboard_input = main_menu()
    if keyboard_input == "1":
        query(True)
        continue  # 通过continue继续下一次循环，一进来就是回到了主菜单
    elif keyboard_input == "2":
        num = int(input("请输入你想存款的金额："))
        deposit(num)
        continue
    elif keyboard_input == "3":
        num = int(input("请输入你想取款的金额："))
        withdrawal(num)
        continue
    else:
        print("程序退出了")
        break  # 通过break退出循环