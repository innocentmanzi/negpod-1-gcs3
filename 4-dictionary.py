#!/usr/bin/python3
def roman_to_int():
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    value = input('enter your roman numeral: ').upper()
    result = 0
    prev_value = 0
    for i in range(len(value) - 1, -1, -1):
        curr_value = roman_values[value[i]]
        if curr_value < prev_value:
            result -= curr_value
        else:
            result += curr_value
        prev_value = curr_value
    return result
print(roman_to_int())
