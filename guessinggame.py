import random

random1 = random.randint(0, 100)
guess = 0
count = 0

while guess != random1 and guess != 'exit':

    guess = input('Try and guess what number your opponant has: ')

    if guess == 'exit':
        break

    guess = int(guess)
    count += 1

    if guess < random1:
        print('Guess is too low')
    elif guess > random1:
        print('Guess is too high')
    else:
        print('You guesses right you luck bastard')
        print(f'And it only took you {count} trys you whore')

        again = input('Do you want to play again y/n?'.format(count, random1))
        if again == 'n' or again == 'exit':
            break
        if again == 'y':
            guess = 0
            count = 0
            random = random.randint(1, 100)

            while again != 'y' and again != 'n' and again != 'exit':
                again = input('y/n? ')
                if again == 'y':
                    guess = 0
                    count = 0
                    random = random.randint(0, 100)
