print('Introduce the number for which you want the list of its divisors')
number = int(input())
divisors = []
for div in range(2, number + 1):
    if number % div == 0:
        divisors.append(div)
print(divisors)