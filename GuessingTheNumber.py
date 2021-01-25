# guessing the number game
import random
n = random.randrange(1, 20)
guess = int(input("enter the number:"))
while n != guess:
    if n < guess:
        print("too high")
        guess = int(input("enter the number:"))
    elif n > guess:
        print("too low")
        guess = int(input("enter the number:"))
    else:
        break
print("you rock :)")
