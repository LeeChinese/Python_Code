"""
演示：元组的定义和操作
元组具有不可修改性
"""
# 定义元组
t1 = (1, "Hello", True)
t2 = ()
t3 = tuple()
print(f"t1的类型是：{type(t1)}，内容是：{t1}")

# 定义单个元素的元素
t4 = ("Hello",)
print(f"t4的类型是：{type(t4)},内容是：{t4}")   # 注意：元组只有一个数据，这个数据后面要添加逗号，否则不是元组类型

# 元组的嵌套
t5 = ( (1, 2, 3), (4, 5, 6))
print(f"t5的类型是：{t5},内容是：{t5}")

# 下标索引去取出内容
num = t5[1][2]
print(f"从嵌套元组中取出的数据是：{num}")

# 元组的操作：index查找方法
t6 = ("程序员", "你好", "Python")
index = t6.index("程序员")
print(f"在元组中查找程序员的下标是：{index}")

# 元组的操作：count统计方法
t7 = ("程序员", "你好", "Python", "程序员")
num = t7.count("程序员")
print(f"统计在元组中程序员的数量是：{num}个")

# 元组的操作：len函数统计元组元素数量
t8 = ("程序员", "你好", "Python", "程序员")
num = len(t8)
print(f"t8元组中的元素有：{num}个")

# 元组的遍历：while
index = 0
while index < len(t8):
    print(f"元组的元素有：{t8[index]}")
    index += 1

# 元组的遍历：for
for element in t8:
    print(f"2元组的元素有：{element}")

# 元组里面的内容不可修改，但是元组里面的列表的内容可以修改