# 1. 定义重复次数计数器
def use_while1():
    i = 1
    while i <= 5:
        print("Hello Python")
        i = i + 1
    print(f'循环结束，i的值{i}')


def use_continue():
    result = 0

    i = 0

    while i <= 100:

        if i % 2 == 1:
            i += 1
            continue
        result += i

        i += 1

    print(f"0~100之间的数字求和结果 = {result} i={i}")


def use_break():
    result = 0

    i = 0

    while i <= 100:

        if result > 2000:
            break
        result += i

        i += 1

    print(f"0~100之间的数字求和结果 = {result} i={i}")


def use_print():
    print("Hello", end='')
    print('world', end=' ')
    print('howareyou')


def use_for():
    my_list = ['ab', 'bd', 'cf', 'haha']
    for i in my_list:
        print(i, end=' ')
    print()
    print('-' * 50)


def use_for_else():
    for i in range(10):  # range是左闭右开
        if i == 15:
            print(f'不会走下面else的内容，找到了{i}')
            break
    else:
        print('没找到')


# use_while1()
# use_continue()
# use_break()
# use_print()
use_for()
# use_for_else()
