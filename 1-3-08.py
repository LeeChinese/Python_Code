# 判断语句的嵌套
age = 20
year = 4
leval = 1
if age >= 18:
    print("你是成年人")
    if age < 30:
        print("你的年龄达标了")
        if year > 2:
            print("恭喜你，年龄和入职时间都达标，可以领取礼物")
        elif leval > 3:
            print("恭喜你，年龄和级别达标，可以领取礼物")
        else:
            print("不好意思，尽管年龄达标，但是入职时间和级别不达标")
    else:
        print("不好意思，年龄太大了")
else:
    print("不好意思，小朋友不可以领取")
