# Project Solutions 📃

This repository contains solutions to the following GCS-3 Problems for Negpod-1:

## Problem 1 🔍

Create a shell script that checks if a file exists or not:
- If the file doesn’t exist it should print 2
- If the file exists:
  - The file can be empty, in this case print 1
  - The file is not empty, in this case print 0


## Solution ✅

The solution to this problem can be found in the [0-shell_script](./0-shell_script) file of this repository. It can be run from the command line as follows:

```sh
user@User:~$ ./0-shell_script [filename]
```
The script will check the file and print the appropriate output based on the status of the file. i.e if it exists, empty or not.

## Problem 2 🔍

Write a Python program that takes an integer input from the user, and performs the following conditional actions:
- If m  is even, print Weird
- If m is odd and in the inclusive range of 2 to 5, print Not Weird
- If m is odd and in the inclusive range of 6 to 20, print Weird
- If m is odd and greater than  20, print Not Weird


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

a) Write a shell script that asks the user for two numbers and outputs their products. The expected output should be a statement as such 

```sh
The product of 3 and 3 is 9.
```
b) Suppose you want to create 4 folders. Create a text file with at least 4 words(folder name on each line). Write a shell script that reads each line of the text file. Then creates a corresponding folder for each folder name.

## Solution ✅

a) The shell script that asks the user for two numbers and ouputs their product is called [product-of_2_numbers](./product-of_2_numbers). It can be run from the command line as follows:

```sh
user@User:~$ ./product-of_2_numbers
```
The script will prompt the user to enter 2 numbers, and then output the product of the 2 numbers, as shown in the example in the problem statement.

b) The shell script that reads each line of a text file [folders.txt](./folders.txt), then creates a corresponding folder for each folder name is called [create-folders](./create-folders). It can be run from the command line as follows:

```sh
user@User:~$ ./create-folders
```
The script will reads each line of the text file [folders.txt](./folders.txt), then creates a corresponding folder for each folder name.

## Problem 5 🔍

Write a shell script that takes a path, and confirms if it is a directory or not. If it is a directory list all files in that directory, if not ask the user to give the file path of a directory.  
- Expected output: List of files in the directory path that was provided

## Solution ✅

The shell script that checks the path and lists the files is [check-and_list_directory](./check-and_list_directory). It can be run from the command line as follows:

```sh
user@User:~$ ./check-and_list_directory
```
The script will prompt the user to enter a path, and then output a list of files in the directory if it is a directory, or ask the user to enter the path of a directory if it is not a directory, as shown below: 
```sh
teniola@Teniola:~/Group-_gcs-2-$ pwd
/home/teniola/Group-_gcs-2-
teniola@Teniola:~/Group-_gcs-2-$ ./check-and_list_directory
Enter a path: /home/teniola/Group-_gcs-2-
The path you entered is a directory
Listing all files in the directory:
total 64
drwxr-xr-x 4 teniola teniola 4096 Feb 17 16:39 .
drwxr-xr-x 6 teniola teniola 4096 Feb 17 16:31 ..
drwxr-xr-x 8 teniola teniola 4096 Feb 17 16:41 .git
-rwxr-xr-x 1 teniola teniola  204 Feb 15 16:15 Problem_1_paterne
-rw-r--r-- 1 teniola teniola 2431 Feb 17 15:49 README.md
-rwxr--r-- 1 teniola teniola  467 Feb 17 14:38 calculate_square_roots
-rwxr-xr-x 1 teniola teniola  585 Feb 17 15:45 check-and_list_directory
-rwxr--r-- 1 teniola teniola  210 Feb 17 14:54 count_words_and_spaces
-rwxr-xr-x 1 teniola teniola  136 Feb 17 15:22 create-folders
-rw-r--r-- 1 teniola teniola   32 Feb 17 15:05 folders.txt
-rw-r--r-- 1 teniola teniola   99 Feb 17 15:54 message_template.txt
-rw-r--r-- 1 teniola teniola   61 Feb 17 15:53 names.txt
-rwxr-xr-x 1 teniola teniola  578 Feb 17 16:28 new-year_message
-rwxr--r-- 1 teniola teniola  204 Feb 17 14:23 print_strings
-rwxr-xr-x 1 teniola teniola  214 Feb 17 15:03 product-of_2_numbers
drwxr-xr-x 6 teniola teniola 4096 Feb 17 16:39 test
teniola@Teniola:~/Group-_gcs-2-$
```

## Problem 6 🔍

Suppose that you want to write the same message to many people except that you want each message personalized with the recipients’ names. This can be achieved using a shell script.

## Solution ✅

The shell script that creates personalized messages for each recipient is [new-year_message](./new-year_message). It can be run from the command line as follows:

```sh
user@User:~$ ./new-year_message
```
The script will read the text file [names.txt](./names.txt), which is in the same directory as the script, and the message template in [message_template.txt](./message_template.txt). It will then create a personalized message for each recipient in a file named after the recipient. For example, if the recipient's name is `Noella`, the file name would be [Noella.txt](./test/Noella.txt). The message in the file will be personalized with the recipient's name, as shown below:

```sh
user@User:~/Group-_gcs-2-/test$ cat Noella.txt
Happy New Year Noella!
May the coming year be full of grand adventures and opportunities.
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
