from itertools import groupby


def sum_even_digits(number):
    return sum(digit * (1 - digit % 2) for digit in map(int, str(abs(number))))

def count_vowel_triplets(text):
    vowels = set('aeiouy')
    text = text.lower()
    return sum(
        (text[i] in vowels) & 
        (text[i+1] in vowels) & 
        (text[i+2] in vowels) 
        for i in range(len(text)-2)
    )

def find_fibonacci_index(number):
    fib = [1, 1]
    while fib[-1] < number:
        fib.append(fib[-1] + fib[-2])
    return (len(fib) * (fib[-1] == number)) - 1


def remove_duplicates(string):
    return ''.join(k for k, _ in groupby(string))

# print(remove_duplicates("aaabbbccca"))