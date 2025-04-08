#!/usr/bin/env python

class Person(object):
    total = 10

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def gatName(self):
        return self.name

    def gatAge(self):
        return self.age

my = Person('Moon', 23)
print(my.name)
print(my.gatAge())
print(my.gatName())
print(my.gatAge())
print(my.total)

you = Person('Lee', 25)
print(you.gatName())
print(you.gatAge())
print(you.total)