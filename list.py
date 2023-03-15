#!/usr/bin/python3

# write a function that takes a list of integers and a target number

def insert():
    nums = list(map(int, input("Enter the list of integers (comma-separated): ").split(",")))
    target = int(input("what is your target: "))
    nums.append(target)
    nums.sort()
    return nums.index(target)
index = insert()
print("Index:", index)
