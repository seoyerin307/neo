#!/usr/bin/env python

def Gcd(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def dgc(self):
        if self.a < self.b:
            self.a, self.b = self.b, self.a
            print("gcd", (self.a, self.b))
            while self.b != 0:
                r = self.a % self.b
                self.a = self.b
                self.b = r
                print("gcd", (self.a, self.b))

a = int(input("Input First number: "))
b = int(input("Input Second number: "))

gcd1 = Gcd(a,b)
print(f'gcd({a},{b}) of {a}, {b} : {gcd1.gcd()}')