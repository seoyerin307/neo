#!/usr/bin/env python

n = int(input("How much number input? : "))

buliding = list(map(int, input().split()))
print("\nmin(buliding) : ", buliding)

min_bulid = min(buliding)
print("\nmin(building) : ", min_bulid)

min_build_n = min(buliding) * n
print("\nmin(building) * n : ", min_build_n)

sum_building = sum(buliding)
print("\nsum(building) : ", sum_building)

result = sum_building - min_build_n
print("\nsum(building) - min(building) * n) : ", result)