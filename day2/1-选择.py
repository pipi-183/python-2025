import random


def use_if():
    # 1. 定义年龄变量
    age = 16

    # 2. 判断是否满 18 岁
    if age >= 18:
        print('允许进入网吧')
    else:
        print("允许进入")

    # 3. 无论条件是否满足都会执行
    print("这句代码什么时候执行?")


def use_elif():
    holiday_name = "情人节"

    if holiday_name == "情人节":
        print("买玫瑰")
        print("看电影")
    elif holiday_name == "平安夜":
        print("买苹果")
        print("吃大餐")
    elif holiday_name == "生日":
        print("买蛋糕")
    else:
        print("每天都是节日")


def use_two_if():
    has_ticket = True

    # 定义整数型变量 knife_length 表示刀的长度，单位：厘米
    knife_length = 21

    # 检查是否有车票，如果有，才允许进行安检
    if has_ticket:
        print("有车票，可以开始安检...")

        # 安检时，需要检查刀的长度，判断是否超过 20 厘米
        # 如果超过 20 厘米，提示刀的长度，不允许上车
        if knife_length >= 20:
            print("不允许携带 %d 厘米长的刀上车" % knife_length)
        # 如果不超过 20 厘米，安检通过
        else:
            print("安检通过")

    # 如果没有车票，不允许进门
    else:
        print("您要先买票")


def use_random():
    player = int(input("请出拳 石头（1）／剪刀（2）／布（3）："))

    # 电脑 随机 出拳
    computer = random.randint(1, 3)
    print(player, computer)
    # 比较胜负
    if ((player == 1 and computer == 2) or
            (player == 2 and computer == 3) or
            (player == 3 and computer == 1)):

        print("赢")
    elif player == computer:
        print("平")
    else:
        print("输")


# use_if()
# use_elif()
# use_two_if()
use_random()
