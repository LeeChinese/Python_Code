"""
练习案例：列表常用功能练习
"""
# 定义一个列表记录一批学生的年龄
student_old = [21, 25, 21, 23, 22, 20]

# 追加一个数字31，到列表的尾部
student_old.append(31)
print(f"追加一个数字31后列表的结果是：{student_old}")

# 追加一个新列表[29, 33, 30]，到列表的尾部
student_old.extend([29, 33, 30])
print(f"追加一个新列表后的结果是：{student_old}")

# 取出第一个元素
num1 = student_old[0]
print(f"取出的第一个元素是：{num1}")

# 取出最后一个元素
num2 = student_old[-1]
print(f"取出最后一个元素是：{num2}")

# 查找元素31，在列表中的下标位置
index = student_old.index(31)
print(f"元素31在列表中的下标位置：{index}")