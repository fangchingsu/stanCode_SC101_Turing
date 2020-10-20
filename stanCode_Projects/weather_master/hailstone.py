"""
File: hailstone.py
Name: Fangching Su
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, as defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    User inputs a number, printing each steps
    that odd is made 3n+1 and even is taken half
    and calculating steps to reach 1
    """
    print("This program computes Hailstone sequences. \n")
    number = int(input("Enter a number: "))

    # the first input number is 1
    if number == 1:
        print("It took 0 steps to reach 1.")
    else:
        # declare variable count
        count = 0
        # use while loops to run the number until it reaches to 1
        while True:
            # use mod% to judge odd or even
            o_or_e = number % 2
            # the number reaches to 1
            if number == 1:
                break
            else:
                # number mod 2 is equal to 1
                if o_or_e == 1:
                    print(str(int(number))+" is odd, so I make 3n+1: " +str(int(3*number+1)))
                    # update the number
                    number = 3*number+1
                # number mod 2 is equal to 0
                else:
                    print(str(int(number)) + " is even, so I take half: " + str(int(number/2)))
                    # update the number
                    number = number/2
                # calculate steps
                count += 1

        # judgement count is 1 or others
        if count == 1:
            print("It took " + str(count) + " step to reach 1.")
        else:
            print("It took " + str(count) + " steps to reach 1.")


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
