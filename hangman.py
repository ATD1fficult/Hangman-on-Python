import random
import string
import sys

def menu_please():
    menu = input("Type 'play' to play the game, 'exit' to quit:").lower()
    if menu == "play":
        hangman()
        if menu == "exit":
            sys.exit()



def hangman():
    print ( 'H A N G M A N\n' )
    words = [ 'python','java','kotlin','javascript' ]
    word_choosen = random.choice ( words ).lower ( )
    lives = 8
    letters_set = set ( word_choosen )
    guess_set = set ( )
    alphabet = set ( string.ascii_lowercase )
    wrong_set = set ( )
    while len ( letters_set ) > 0 and lives > 0 :
        word_list = [ letter if letter in guess_set else '-' for letter in word_choosen ]
        print ( '' )
        print ( ''.join ( word_list ) )
        user_input = input ( 'Input a letter:' )
        if len ( user_input ) > 1 :
            print ( 'You should input a single letter' )
            continue
        if user_input not in alphabet :
            print ( 'Please enter a lowercase English letter' )
            continue
        if user_input in alphabet :
            if user_input in letters_set :
                guess_set.add ( user_input )
                letters_set.remove ( user_input )
                if len ( letters_set ) == 0 :
                    print ( 'You guessed the word!' )
                    print ( 'You survived!' )
                    break
                continue
            if user_input in wrong_set :
                print ( "You've already guessed this letter" )
                continue
            if user_input in guess_set and user_input not in letters_set or user_input in wrong_set :
                print ( "You've already guessed this letter" )
                wrong_set.add ( user_input )
            if user_input not in letters_set and user_input not in guess_set :
                print ( "That letter doesn't appear in the word" )
                wrong_set.add ( user_input )
                lives -= 1
        if lives == 0 :
            print ( 'You lost!' )

menu_please()

