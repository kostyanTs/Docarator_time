import time
import timeit

def timer(fn):
    def wraper():
        res = fn()
        find_time = timeit.timeit(res, number = 100)/100
        return find_time
    return wraper

@timer
def Hello():
    print("Hello World")