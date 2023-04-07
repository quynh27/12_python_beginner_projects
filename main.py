import random
def guess(x):
    random_number = random.randint(1,x)
    guess =0
    while guess != random_number:
        guess= int(input(f"guess a number between 1 and {x} "))
        if guess < random_number :
            print("your guess is less than the random number")
        if guess >  random_number:
            print("your guess is more than the random number")
    
    print("congrats that is correct! ")


def computer_guess(x):
    low = 1
    high =x
    feedback = ''
    
    while feedback != 'c':
        guess= random.randint(low,high)
        feedback=input(f"is the {guess} too low (l) or too high(h) or correct (c)?".lower())
        if feedback=='l':
            low= guess+1
        elif feedback=='h':
            high = guess-1
    
    print(f"you just guessed the {guess} , which is correct! ")





print("hallo!")
computer_guess(10)



