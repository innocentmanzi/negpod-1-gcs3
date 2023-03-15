#!/usr/bin/python3
n = int(input("Enter an integer: "))
for i in range(1, n+1):
    if i % 2 == 1:
        print(i, end=" ")
print("Output: ", i)
