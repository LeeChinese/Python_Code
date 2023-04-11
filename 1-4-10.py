"""
演示：for循环的嵌套使用
"""
# 坚持表白100天，每天都送10朵花

# 定义全局变量i
i = 0
for i in range(100):
    print(f"今天是表白的第{i + 1}天")

    # 写内层循环
    for x in range(10):
        print(f"今天送的第{x + 1}朵花")
    print("我喜欢你")

print(f"第{i + 1}天，表白成功")