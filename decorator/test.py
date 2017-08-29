#coding: utf-8

import functools

"""
@file: test.py
@time: 2017/8/28 
@author: chenfan
"""

def deco(func):
    print "before base called"
    func()
    print "after base called"
    return func

def func():
    print "base func"

func = deco(func)#替换函数（装饰）

#语法糖装饰
@deco
def func2():
    print "base func2"
func2()

print "-----------------------分割线---------------------"

def deco3(func):
    def wrapper(*args,**kwargs):
        print "%s is running" %func.__name__
        return func(*args,**kwargs)
    return wrapper

@deco3
def func3():
    print "this is base func3"
func3()

print "-----------------------分割线---------------------"

##带参数的装饰器
def deco4(level):
    def decorator(func):
        def wrapper(*args,**kwargs):
            if level == 'error':
                print "%s is running" % func.__name__
            return func(*args, **kwargs)
        return wrapper
    return decorator
@deco4(level='error')
def func4():
    print  "base func4"
func4()

def deco42():
    def decorator(func):
        def wrapper(*args,**kwargs):
            print "%s is running" % func.__name__
            return func(*args, **kwargs)
        return wrapper
    return decorator
@deco42()
def func42():
    print  "base func4"
func4()

print "-----------------------分割线---------------------"
##类装饰器
class deco5(object):
    def __init__(self,func):
        self._func = func

    def __call__(self):
        print "class deco  running"
        self._func()
        print "class deco ending"

@deco5
def func5():
    print "base func5"
func5()

print "-----------------------分割线---------------------"
#保留源方法信息
#functools.wraps
def deco6():#未传参
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            print "deco6 runnning"
            func()
            print "deco6 ending"
        return wrapper
    return decorator
@deco6()   ##带参数是为deco6(),参数为空
def func6():
    print "base func6"
func6()

##不传参
def deco7(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print "deco7 runnning"
        func()
        print "deco7 ending"
    return wrapper
@deco7 ##不传参数
def func7():
    print "base func7"
func7()