"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'  # This is the filename of an English dictionary
EXIT = '-1'  # Controls when to stop the loop
save_word = []


def main():
    print(f'Welcome to stanCode "Anagram Generator" (or {EXIT} to quit)')
    while True:
        vac = input("Find anagrams for: ")
        if vac == EXIT:
            break
        else:
            print("Searching...")
            find_anagrams(vac)


def read_dictionary():
    global save_word
    with open(FILE, 'r') as f:
        for line in f:
            words = line.split()
            save_word += words


def find_anagrams(s):
    """
    :param s:
    :return:
    """
    alpha_s = []
    w_list = []
    index = []
    read_dictionary()
    for alphabet in s:
        alpha_s += alphabet
    find_anagrams_helper(alpha_s, [], len(s), w_list, index)
    print(f'{len(w_list)} anagrams: {w_list}')


def find_anagrams_helper(alpha_s, cur_lst, word_len, w_list, index):
    word = ""
    if len(cur_lst) == word_len:
        for i in range(len(cur_lst)):
            word += cur_lst[i]
        if word in save_word:
            if word not in w_list:
                print(f'Found: {word}')
                w_list.append(word)
                print("Searching...")
    else:
        for i in range(len(alpha_s)):
            sub_s = ""
            if i not in index:
                index.append(i)
                # choose
                cur_lst.append(alpha_s[i])
                # explore
                for j in range(len(cur_lst)):
                    sub_s += cur_lst[j]
                if has_prefix(sub_s):
                    find_anagrams_helper(alpha_s, cur_lst, word_len, w_list, index)
                # un-choose
                cur_lst.pop()
                index.pop()


def has_prefix(sub_s):
    """
    :param sub_s:
    :return:
    """
    for w in save_word:
        if w.startswith(sub_s):
            return True


if __name__ == '__main__':
    main()
