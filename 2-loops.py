#!/usr/bin/python3
# python program to print all odd numbers up to the integer

num = int(input("Input any number: "))
print("Input: {}".format(num))

for i in range(1, num + 1, 2):
    if i % 2 == 1:
        print("Output: ", i, end=",")
