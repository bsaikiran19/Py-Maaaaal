import random #random word generator

name = input("What is your name? ")

print("Good Luck ! ", name)

words = ['Alpha', 'Achutiya', 'Maths', 'carbon',
         'python', 'hero', 'player', 'pookies',
         'reverse', 'water', 'board', 'handsome']

word = random.choice(words)   #random generator kr ta h yeh 

print("Guess the characters")
#guesses are limited change krna h toh  change the value og turns...
guesses = ''
turns = 12

while turns > 0:

    failed = 0

    for char in word:

        if char in guesses:
            print(char, end=" ")

        else:
            print("_")
            failed += 1

    if failed == 0:
        print("You Win")
        print("The word is: ", word)
        break

    print()
    guess = input("guess a character:")

    guesses += guess

    if guess not in word:

        turns -= 1
        print("Wrong")
        print("You have", + turns, 'more guesses')

        if turns == 0:
            print("You Loose")
