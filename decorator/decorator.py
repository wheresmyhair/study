'''
需求：在函数执行前打印before，在执行后打印after
'''
import functools

def outer(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print("before")
        value = func(*args, **kwargs)
        return value
    return inner

@outer
def func(a1):
    print("hello world")
    value = (1,2,3,4)
    return value

@outer("world")
def func2(a1, a2):
    print("hello world2")
    value = [1,2,3,4]
    return value

print(func(1))
print(func2(1,1))