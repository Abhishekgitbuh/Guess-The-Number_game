# Number Guessing Game
'''
 The number of guesses should be limited, i.e (5 or 9).
 Print the number of guesses left.
 Print the number of guesses he took to win the game.
 “Game Over” message should display if the number of guesses becomes equal to 0.'''
import random

guess = 9
n = random.randrange(0, 100, 3)
print(n)
while 1:
    if guess == 0:
        print("Game Over!!")
        break
    print("number of guesses left =", guess)
    a = int(input("Enter a random number between 0 and 100 : "))
    if a < n:
        print("increase")
    elif a > n:
        print("decrease")
    if a == n:
        print("superb, you have won!\nyou have taken", 10-guess, "guesses to win this game.")
        break
    else:
        guess = guess - 1
