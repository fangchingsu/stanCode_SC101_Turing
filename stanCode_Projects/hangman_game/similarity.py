"""
File: similarity.py
Name: Fangching Su
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    TODO: input long DNA sequence and short DNA sequence and call the function to fnd the similarity between two DNA sequences
    """
    # input the DNA sequence
    long_seq = input("Please give me a DNA sequence to search: ").upper()
    short_seq = input("What DNA sequence would you like to match? ").upper()
    # call the function
    ans = compare(long_seq, short_seq)
    # print answer
    print("The best match is " + ans)


def compare(long_seq, short_seq):
    # calculate compare times
    compare_time = len(long_seq) - len(short_seq) + 1
    count = 0
    best_string = ""
    # run compare times
    for i in range(compare_time):
        # separate long sequence to short sequence length
        sep_long_seq = long_seq[i:len(short_seq)+i]
        save_count = 0
        # compare the each separate long sequence and short sequence
        for j in range(len(sep_long_seq)):
            for k in range(len(short_seq)):
                # calculate the char in separate long sequence equal to short sequence
                if short_seq[k] == sep_long_seq[k]:
                    save_count += 1
        # get the greatest count value and matched string
        if save_count > count:
            count = save_count
            best_string = sep_long_seq
    # return value
    return best_string


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
