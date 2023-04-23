"""
演示数据容器：list列表的常用操作
"""
mylist = ["itcast", "itheima", "python"]
# 查找某元素在列表内的下标索引
index = mylist.index("python")
print(f"python在列表中的下标索引值是：{index}")
# 如果被查找的元素不存在，会报错
# index = mylist.index("hello")
# print(f"hello在列表中的下标索引值是：{index}")

# 修改特定下标索引的值
mylist[0] = "best"
print(f"列表被修改元素值后，结果是：{mylist}")

# 在列表中加入一个特定的元素 语法：列表.insert()
mylist.insert(2, "hello")
print(mylist)

# 在列表的尾部追加‘’‘单个’‘’新元素
mylist.append("程序员")
print(f"列表在追加了元素后，结果是：{mylist}")

# 在列表的尾部追加‘’‘一批’‘’新元素
mylist2 = [1, 2, 3]
mylist.extend(mylist2)
print(f"列表在追加了一个新列表后，结果是：{mylist}")

# 删除指定下标索引的元素 （2种方式）
mylist = ["itcast", "itheima", "python"]
# 方式1：del 列表[下标]
del mylist[2]
print(f"列表删除元素后结果是：{mylist}")
# 方式2：列表.pop(下标)
mylist = ["itcast", "itheima", "python"]
element = mylist.pop(2)
print(f"通过pop方法取出元素后列表内容是：{mylist}，取出的元素是：{element}")

# 删除某元素在列表中的第一个匹配项
mylist = ["itcast", "itheima", "itcast", "itheima", "python"]
mylist.remove("itcast")
print(f"通过remove方法移除元素后，列表的结果是：{mylist}")

# 清空列表
mylist.clear()
print(f"列表被清空了，结果是：{mylist}")

# 统计列表内某元素的数量
mylist = ["itcast", "itheima", "itcast", "itheima", "python"]
count = mylist.count("itcast")
print(f"列表中itcast的数量是：{count}")

# 统计列表中全部的元素数量
mylist = ["itcast", "itheima", "itcast", "itheima", "python"]
count = len(mylist)
print(f"列表的元素数量总共有：{count}个")