"""
演示python中
if-else的组合判断语句
"""
age = int(input("请输入你的年龄："))

if age >= 18:
    print("您已成年，需要买票10元。")
else:  # else不需要判断条件，当if的条件不满足时，else执行
    print("您未成年，可以免费游玩。")

print("祝您游玩愉快。")