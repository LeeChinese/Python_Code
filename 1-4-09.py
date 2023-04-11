"""
如果在for循环外部访问临时变量：
实际上是可以访问到的
在编程规范上，是不允许的、不建议这么做
"""
i = 0
for i in range(5):
    print(i)

print(i)