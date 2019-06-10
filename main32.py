import random

level = int(raw_input("Pick a difficulty level (1, 2, or 3)"))
max_value = None
if level ==1:
    max_value = 10
elif level ==2:
    max_value = 100
else:
    max_value=1000

mynumber = random.randint(1,max_value)
guess = int(raw_input("I have my number. What's your guess?"))
guesscount = 1

while guess != mynumber:
    if guess < mynumber:
        print "Too low. Guess again"
    else:
        print "Too high. Guess again"
    guess = int(raw_input())
    guesscount += 1

print "You got in in", guesscount