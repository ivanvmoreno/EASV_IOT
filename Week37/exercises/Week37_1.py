from datetime import datetime

print('Introduce your Name')
name = input()
print('Introduce your age')
age = int(input())
curr_year = datetime.today().year
centenary = curr_year + (100 - age)
print("%s, you'll turn 100 in %d!" % (name, centenary))