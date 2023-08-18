from functools import reduce

nums = [2, 4, 13, 6, 29, 73, 99, 34, 91, 88, 10, 31, 143, 820, 777, 811, 9]


even_nums = list(filter(lambda n: n % 2 == 0, nums))
odd_nums = list(filter(lambda n: n % 2 == 1, nums))
print(f"The odd numbers in the list are: {odd_nums}")
print(f"The even numbers in the list are: {even_nums}")

print(__name__)
