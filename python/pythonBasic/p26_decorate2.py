#!/usr/bin/env python
import datetime

def datetime_deco(func):

    def decorated():
        print(datetime.datetime.now())
        func()
        print(datetime.datetime.now())
        print()
    return decorated

@datetime_deco
def func1():
    print('Main function1 start')

def func2():
    print('Main function2 start')

def func3():
    print('Main function3 start')

func1()
func2()
func3()


