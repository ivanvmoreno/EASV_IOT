from random import randint

number = randint(0, 10)
match = False

while type(match) != int:
    print("What's your guess?")
    guess = int(input())
    if guess < number:
        print('Too low! Try again')
    elif guess > number:
        print('Too high! Try again')
    else:
        match = guess 
print("You did it! The number is %s" % match)