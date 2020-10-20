"""
File: boggle.py
Name: Fangching Su
----------------------------------------
TODO:
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
dict_word = []
# SEARCH = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def main():
    """
    TODO:
    """
    grid = [[], [], [], []]
    end = True
    for i in range(4):
        input_row = input(f'{i + 1} row of letters:').lower()
        alpha = input_row.split(" ")
        grid[i] = alpha
        for j in range(4):
            if len(alpha) == 4 and len(alpha[j]) == 1 and alpha[j].isalpha():
                pass
            else:
                print("Illegal Input")
                end = False
                break
        # stop double loop
        if not end:
            break
    read_dictionary()
    find_voc(grid)


def find_voc(grid):
    word_list = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            used = []
            word = grid[y][x]
            used.append((y, x))
            find_voc_helper(grid, word, y, x, used, word_list)
    print(f'There are {len(word_list)} words in total.')


def find_voc_helper(grid, word, y, x, used, word_list):
    if len(word) > 3:
        if word not in word_list:
            if word in dict_word:
                word_list.append(word)
                print(f'Found: {word}')
    if not has_prefix(word):
        pass
    else:
        # start from current letter
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                # for dy, dx in SEARCH:
                ny = y + dy
                nx = x + dx
                # make sure nx, ny in the range
                if ny < 0 or ny > 3 or nx < 0 or nx > 3:
                    pass
                else:
                    if (ny, nx) not in used:
                        # choose
                        used.append((ny, nx))
                        word += grid[ny][nx]
                        # explore
                        find_voc_helper(grid, word, ny, nx, used, word_list)
                        # un-choose
                        used.pop()
                        word = word[:len(word) - 1]


def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    """
    global dict_word
    with open(FILE, 'r') as f:
        for line in f:
            words = line.split()
            dict_word += words


def has_prefix(sub_s):
    """
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    for w in dict_word:
        if w.startswith(sub_s):
            return True


if __name__ == '__main__':
    main()
