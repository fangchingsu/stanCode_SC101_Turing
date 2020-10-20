"""
File: hangman.py
Name: Fangching Su
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
to try in order to win this game.
"""
import random
# This constant controls the number of gtuess the player has
N_TURNS = 7


def main():
    """
    TODO:
    """
    answer = ""
    old_char = ""
    # get the word from random_word function
    for i in random_word():
        answer += i
        old_char += "-"
    # assign old_char String value to update_char String
    update_char = old_char
    print("The word look likes " + old_char)
    # can guess n turns
    for i in range(N_TURNS, 0, -1):
        # already get the answer, do nothing until i to 1
        if update_char == answer:
            break
        else:
            print("You have " + str(i) + " guesses left.")
            #
            while update_char != answer:
                guess = input("Your guess: ").upper()
                # judge correct input
                if guess.isalpha() and len(guess) == 1:
                    # find guess char in answer
                    check_find = answer.find(guess)
                    # judge find the char
                    if check_find == -1:
                        print("There is no " + guess + "'s in the word.")
                        print("The word look likes " + update_char)
                        # no turns
                        if i == 1:
                            print("Your are completely hung :(")
                            print("The word was " + answer)
                        break
                    else:
                        print("You are correct!")
                        # update update_char String
                        for j in range(len(answer)):
                            ans = ''
                            count = 0
                            # get char in answer
                            ch = answer[j]
                            # update guess char to update_char String
                            if guess == ch:
                                ans += update_char[:j]
                                ans += guess
                                ans += update_char[j+1:]
                                update_char = ans
                        print("The word look likes " + update_char)
                        # when get the answer
                        if update_char == answer:
                            print("You win!!")
                            print("The word was: " + answer)
                else:
                    print("Illegal format.")


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
