number = 4
guess = int(input("Care to play a game? Can you guess what number I am thinking of? Please enter any number: "))
while number!= guess:
    if guess < number:
        print("Too low")
        guess = int(input("Try again: "))
    elif guess > number:
        print("Too high!")
        guess = int(input("Try again: "))
    else:
        break
print("You guessed it right! Congratulations!")
