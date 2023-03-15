#!/usr/bin/python3
# python program to print all odd numbers up to the integer

num = int(input("Input any number: "))
print("Input: {}".format(num))

odd_numbers = []
for i in range(1, num + 1, 2):
    odd_numbers.append(str(i))

print("Output: " + ", ".join(odd_numbers))
