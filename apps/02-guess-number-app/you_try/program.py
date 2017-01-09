import random

title_len = 40

print('-' * title_len)
print('GUESS THE NUMBER APP'.center(title_len))
print('-' * title_len)
print()

target = random.randrange(101)

num = int(input('Guess a number between 0 and 100: '))
#print('Your number is: ' + str(num))
#print('Target number is: ' + str(target))

while num != target:
    if num > target:
        print('Sorry, but {} is HIGHER than the number'.format(num))
    elif num < target:
        print('Sorry, but {} is LOWER than the number'.format(num))

    num = int(input('Guess a number between 0 and 100: '))
else:
    print("YES! You've got it. The number is {}".format(num))
