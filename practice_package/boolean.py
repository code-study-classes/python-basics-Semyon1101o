def check_between_numbers(A, B, C):
    return (A < B < C) or (C < B < A)

def check_odd_three(number):
    return (100 <= abs(number) <= 999) and (number % 2 != 0)

def check_unique_digits(number):
    return (100 <= abs(number) <= 999) * (len(set(str(abs(number)))) == 3) == 1

def check_palindrome_number(number):
    str_number = str(abs(number))
    return str_number == str_number[::-1]

def check_ascending_digits(number):
    str_number = str(number)
    return (100 <= number <= 999) * (str_number[0] < str_number[1] < str_number[2])
