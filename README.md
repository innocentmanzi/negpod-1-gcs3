# Project Solutions 📃

This repository contains solutions to the following GCS-3 Problems for Negpod-1:

## Problem 1 🔍

Create a shell script that checks if a file exists or not:
- If the file doesn’t exist it should print `2`
- If the file exists:
  - The file can be empty, in this case print `1`
  - The file is not empty, in this case print `0`


## Solution ✅

The solution to this problem can be found in the [0-shell_script](./0-shell_script) file of this repository. It can be run from the command line as follows:

```sh
user@User:~$ ./0-shell_script [filename]
```
The script will check the file and print the appropriate output based on the status of the file. i.e if it exists, empty or not.

## Problem 2 🔍

Write a Python program that takes an integer input from the user, and performs the following conditional actions:
- If `m`  is even, print `Weird`
- If `m` is odd and in the inclusive range of `2` to `5`, print `Not Weird`
- If `m` is odd and in the inclusive range of `6` to `20`, print `Weird`
- If `m` is odd and greater than  `20`, print `Not Weird`


## Solution ✅

The Python script for this problem is [1-if.py](./1-if.py) in the repository. To run the script, use the following command:

```sh
user@User:~$ ./1-if.py
```
The script will prompt the user to enter an integer and then print the corresponding output based on the conditions specified in the problem statement.

## Problem 3 🔍

Write a Python program that takes an integer and prints all odd numbers up to that integer. The program should take the input integer from the user and output the odd numbers in a comma-separated format.

Example:
```sh
Input any number: 5
Input: 5
Output: 1, 3, 5
```

## Solution ✅

The Python program that prints all odd numbers up to the input integer is called [2-loops.py](./2-loops.py). It can be run from the command line as follows:

```sh
user@User:~$ python 2-loops.py

```
The program will prompt the user to enter an integer, and then output all the odd numbers up to that integer in a comma-separated format.

If the user inputs 5, the program will output 1, 3, 5, as shown in the example in the problem statement. The solution code is already available in the [2-loops.py](./2-loops.py) file.

## Problem 4 🔍

Write a python function that takes as parameters a list of integers and a target value, it sorts the list in ascending order and returns the index if the target is found. If not, return the index where it would be if it were inserted in order.

The table below shows a list of inputs you should pass to your function and the expected results. If you get anything other than the expected result, then your function is not correct and you should correct it.

| Input                | Expected Output |
|----------------------|----------------|
| `nums = [1,3,5,6]`, `target = 5` | `2` |
| `nums = [1,3,5,6]`, `target = 2` | `1` |
| `nums = [1,3,5,6]`, `target = 7` | `4` |



## Solution ✅

The Python function that sorts the list and returns the index of the target value or the index where it would be inserted is [3-loops.py](./3-loops.py). It can be run from the command line as follows:
```sh
user@User:~$ python3 3-loops.py
```

The function will prompt the user to enter a comma-separated list of integers and the target value. It will then sort the list in ascending order, and return the index of the target value if it is found, or the index where it would be inserted in order if it is not found. Here is an example of the function being run:
```sh
user@User:~$ python3 3-loops.py
Enter the list of integers (comma-separated): 1,3,5,6
what is your target: 5
Index: 2
```

If you want to test the function with the other inputs provided in the table above, simply replace the values in the `nums` and `target` variables in the `insert` function and run the script again.

## Problem 5 🔍

Write a python function that takes a Roman numeral as input and converts it to an integer. Roman numerals are represented by the symbols in the table below. The conversion should be done according to the rules specified in the problem statement.

| Symbol | Value |
|--------|-------|
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

The function should satisfy the following constraints:

- 1 <= len(s) <= 15 where s is the Roman numeral.

## Solution ✅

The python function that satisfies the requirements of the problem statement is called `roman_to_int` and can be found in the [4-dictionary.py](./4-dictionary.py) file.. It can be run from the command line as follows:

```sh
user@User:~$ ./4-dictionary.py
```
The function will prompt the user to enter a Roman numeral, it will then convert it to an integer. Here is an example of the function being run:
```sh
user@User:~$ python3 4-dictionary.py
enter your roman numeral: XIX
19
```

## Collaborators 🤝

- [Sadick Achuli](https://github.com/Sadickachuli)
- [Abdulhameed Teniola Ajani](https://github.com/Elhameed)
- [Noella Uwayo](https://github.com/n-uwayo)
- [Iraduhaye Paterne](https://github.com/IraduhayeBukuruPaterne1)
- [Innocent Manzi](https://github.com/innocentmanzi)
- [Iranzi Prince](https://github.com/iranziprince01)
- [Mohammed Yasin](https://github.com/MohamedAYasin)
- [Sabir Walid](https://github.com/SabirWalid)
