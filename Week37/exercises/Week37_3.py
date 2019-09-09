ELEMENTS = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print('I want to filter all numbers higher than... (introduce a number)')
max_value = int(input())
print(list(filter(lambda e: e < max_value, ELEMENTS)))