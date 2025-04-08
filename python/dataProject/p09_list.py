#!/usr/bin/env python

numbers = [0, 1, 2, 3]
names = ['kim', 'Lee', 'Park', 'Choi']
print(numbers[0])
print(names[2:])
print(numbers[-1])
print(numbers+names)
empty=[]
print(empty)

names.append('Moon')
print(names)

names.remove('Moon')
print(names)

value = names.pop()
print(value)

value = names.pop(1)
print(value)

numbers.extend([4, 5, 6, 4, 4, 5, 6])
print(numbers)

print(numbers.count(4))

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

numbers.clear()
print(numbers)
