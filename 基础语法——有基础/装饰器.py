# 实现一个装饰器，在开始执行函数时输出该函数名称， 并在结束时输出函数的开始时间和结束时间以及运行时间

import time
import datetime

def decorator(func):
    def wrapper(*args, **kwargs):
        print(f"函数名称：{func.__name__}")

        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        print(f"开始时间：{datetime.datetime.fromtimestamp(start_time)}")
        print(f"结束时间：{datetime.datetime.fromtimestamp(end_time)}")
        print(f"运行时间：{(end_time - start_time)}秒")

        return result

    return wrapper

@decorator
def my_function():
    # 函数体
    time.sleep(2)

my_function()