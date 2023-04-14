"""
演示：列表定义语法
"""
# 注意：列表可以一次存储多个数据，且可以为不同的数据类型，支持嵌套

# 定义一个列表list
my_list = ["itheima", "itcast", "python"]
print(my_list)
print(type(my_list))

my_list = ["itheima", 666, True]
print(my_list)
print(type(my_list))

# 定义一个嵌套的列表
my_list = [[1, 2, 3], [4, 5, 6]]
print(my_list)
print(type(my_list))