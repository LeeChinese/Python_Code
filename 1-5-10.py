
"""
演示变量在函数中的作用域
"""


# 演示局部变量
def test_a():
    num = 100
    print(num)


test_a()
# 出了函数体，局部变量就无法使用了
# print(num)

# 演示全局变量
num = 200


# 定义函数test_b
def test_b():
    print(f"test_b:{num}")


# 定义函数test_c
def test_c():
    print(f"test_c:{num}")


# 调用函数tests_b和test_c
test_b()
test_c()
# 打印num
print(num)

# 在函数内修改全局变量
# global关键字，在函数内声明变量为全局变量
num = 200


# 定义函数test_b
def test_b():
    print(f"test_b:{num}")


# 定义函数test_c
def test_c():
    global num
    num = 500
    print(f"test_c:{num}")


# 调用函数tests_b和test_c
test_b()
test_c()
# 打印num
print(num)