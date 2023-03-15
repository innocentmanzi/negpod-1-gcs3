#!/usr/bin/python3
m = int(input("Input a number: "))
if m % 2 == 0:
   print("Weird")


elif m % 2 != 0 and m in range(2,6):
   print("Not weird")


elif m % 2 != 0 and m in range(6,21):
   print("Weird")
else:
   print("Not Weird")
