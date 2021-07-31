import random
randNumber = random.randint(1,50)
# print(randNumber)
userGuess = None
guesses = 0

print("Welcome To The Perfect Guess Game")

# Test for Results

while(userGuess != randNumber):
    userGuess = int(input("Enter your guess: "))
    guesses += 1
    if(userGuess==randNumber):
        print("Congrats You win...!!!")
    else:
        if(userGuess>randNumber):
            print("You guessed it wrong..!! Enter a smaller number")
        else:
            print("You guessed it wrong..!! Enter a larger number")

print(f"You guesses the number in {guesses} guesses")

with open("hiscore.txt",'r') as f:
    hiscore = int(f.read())

if(guesses<hiscore):
    print("You have just broken the High Score...!!!")
    with open('hiscore.txt','w') as f:
        f.write(str(guesses))