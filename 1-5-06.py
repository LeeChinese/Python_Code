'''
演示函数的返回值定义语法
'''


# 定义一个函数,完成2数相加的功能
def add(a, b):
    result = a + b
    # 通过返回值,将相加的结果返回给调用者
    return result
# 注意:函数体在遇到return后就结束了,所以写在return后的代码不会执行


# 函数的返回值,可以通过变量去接收
r = add(4, 5)
print(r)