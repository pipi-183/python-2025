from module1 import test1
from module2 import test1 as module2_test1
import random

test1()
module2_test1()

print(random.__file__)  # 查看模块所在路径
random.randint(1, 3)
