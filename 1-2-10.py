"""
多个变量占位
彼岸两要用括号括起来
并按照占位的顺序填入
"""

# 通过占位的形式，完成拼接
name = "程序员"
message = "有前途：%s" % name
print(message)

# 通过占位的形式，完成数字和字符串的拼接
class_num = 2030  # class是关键字，不能直接用它定义变量
avg_salary = 50000
message = "Python大数据学科，河南%s期，毕业平均工资%s" % (class_num, avg_salary)
print(message)

"""
Python中，其实支持非常多的数据类型占位
最常用的是如下三类
%s   将内容转换成字符串，放入占位位置
%d   将内容转换成整数，放入占位位置
%f   将内容转换成浮点型，放入占位位置
"""
name = "李氏集团"
setup_year = 2008
stock_price = 19.99
message = "%s,成立于：%d年，我今天的股价是：%f元" % (name, setup_year, stock_price)
print(message)