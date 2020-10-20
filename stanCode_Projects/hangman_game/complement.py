"""
File: complement.py
Name: Fangching Su
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    TODO: input the DNA and call the function to transfer it
    """
    # input the DNA
    dna = input("Please give me a DNA strand and I'll find the complement: ").upper()
    # call function
    ans = build_complement(dna)
    # print answer
    print("The complement of " + dna + " is " + ans + ".")


def build_complement(dna):
    # empty string
    dna_t = ""
    # char in dna
    for i in dna:
        # judge the word and transfer
        if i == 'A':
            dna_t += 'T'
        elif i == 'T':
            dna_t += 'A'
        elif i == 'G':
            dna_t += 'C'
        elif i == 'C':
            dna_t += 'G'
    # return value
    return dna_t


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
