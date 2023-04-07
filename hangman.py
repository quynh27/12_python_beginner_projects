import random
import string
from words import words

def get_a_valid_word(list):
    word = random.choice(list)
    while ' ' in word  or '-' in word:
        word = random.choice(list)
        
    return word

    


def hangman():
    word = get_a_valid_word(words)
    word= word.upper()

    word_characters = list(word)
    print(word_characters)
    alphabet = set(string.ascii_uppercase)
    print(alphabet)
    used_chars = set()

    

    while len(word_characters)>0:
        print('you have guess ', ' '.join(used_chars))

        
        word_list= [char if char in used_chars else '-' for char in word]
        print('the current word is ',' '.join(word_list) )

        user_char= input("guess a char ").upper()



        if user_char in alphabet-used_chars:
            used_chars.add(user_char)
            if user_char in word_characters:
                word_characters.remove(user_char)
        elif user_char in used_chars:
            print('you have guessed this char already, please try again')
        else:
            print('your guess is invalid')

    print('you have won!, the result is '+ word)

    



   
   
hangman()




