"""
File: caesar.py
Name: Fangching Su
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""
# This constant shows the original order of alphabetic sequence
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    TODO: input number and String and call the function
    """
    # input number and String
    sec_num = int(input("Secret number: "))
    ciph_str = input("What's the ciphered string? ").upper()
    # call the function
    deciphered(sec_num, ciph_str)


def deciphered(sec_num, ciph_str):
    new_alphabet = ""
    # switch the alphabet and save to new String
    new_alphabet += ALPHABET[sec_num:]
    new_alphabet += ALPHABET[:sec_num]
    print("The deciphered string is: ", end="")
    # run in ciphered String
    for i in ciph_str:
        # find the alphabet in ALPHABET
        ch = ALPHABET.find(i)
        answer = ""
        # jude i is alpha or not
        if i.isalpha():
            # save the corresponding number in new alphabet String to answer
            answer += new_alphabet[ch]
        else:
            answer += i
        print(answer, end="")


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
