import random


def is_won(player, opponent):
    if(player =='r' and opponent == 's') or (player =='p'and opponent == 'r') or ( player =='s' and opponent == 'p'):
        return True
    return False



def play():
    user = input('what is your choice? r is for rock, p is for paper and s is for scissors  ' )
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'it is even'
    
    if is_won(user, computer):
        return 'you won!'
    
    return 'you lost!'

print(play())


