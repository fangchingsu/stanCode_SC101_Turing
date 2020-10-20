"""
File: quadratic_solver.py
Name: Fangching Su
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""

import math


def main():
	"""
	input parameters of Quadratic equation and find the roots
	"""
	print("stanCode Quadratic Solver!")
	# use while loops to judge a is zero or not
	while True:
		a = int(input("Enter a: "))
		if a == 0:
			print("\"a\" can't be zero.")
		else:
			break
	b = int(input("Enter b: "))
	c = int(input("Enter c: "))
	# calculate discriminant result
	discriminant = b*b - 4*a*c

	# judge the discriminant result
	if discriminant > 0:
		sqrt = math.sqrt(discriminant)
		two_roots_1 = (-1*b+sqrt)/(2*a)
		two_roots_2 = (-1*b-sqrt)/(2*a)
		print("Two roots: " + str(two_roots_1) + ", " + str(two_roots_2))
	elif discriminant == 0:
		one_root = -1*b/2/a
		print("One root: " + str(one_root))
	else:
		print("No real root")

###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
