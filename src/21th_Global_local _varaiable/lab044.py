# #i want  to print log time
# import time
# from turtledemo.penrose import start
#
#
# def time_decorator(func):
#     def wrapper():
#         start_time=time.time()
#         print(start_time)
#         func()
#         end_time=time.time()
#         print(end_time)
#         print("Total_time",end_time-start_time)
#     return wrapper()
#
# @time_decorator
# def start_ui_1():
#     print("Add a function ,The time taken by the function")
#     time.sleep(2)
# @time_decorator
# def start_ui_2():
#     print("Add a function, the time taken by the function")
#     time.sleep(5)
import time
def time_decorator(func):
    def wrapper():
        start_time=time.time()
        print("start_time",start_time)
        func()
        end_time=time.time()
        print("end_time",end_time)
        print("total_time",end_time-start_time)
    return wrapper()

def print_logs(second):
    def wrapper():
        print("start log")
        second()
        print("end log")
    return wrapper()


@time_decorator
@print_logs
def test_ui1():
    print("Add a function,The time taken by the function")
    time.sleep(2)
@time_decorator
@print_logs
def test_ui2():
    print("Add a function,The time taken by the function")
    time.sleep(5)
