"""
File: rocket.py
Name: Fangching Su
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""
# CONSTANT
SIZE = 9


def main():
	"""
	TODO: call each function
	"""
	head()
	belt()
	upper()
	lower()
	belt()
	head()


# head part
def head():
	# run size times
	for i in range(1, SIZE+1):
		# separate two for loop
		# left part
		for j in range(-SIZE+i, i+1):
			# judge when to print '/'
			if j > 0:
				print("/", end="")
			else:
				print(" ", end="")
		# right part
		for k in range(1, i+1):
			print("\\", end="")
		print()


# belt part
def belt():
	print("+",end="")
	# judge need to print how many '='
	for i in range(0, SIZE*2):
		print("=", end="")
	print("+")


# upper part
def upper():
	# print SIZE line "|"
	for i in range(1, SIZE+1):
		print("|", end="")
		# separate two for loop
		# left part
		for j in range(-SIZE+i+1, i+1):
			# judge when to print '/\'
			if j > 0:
				print("/", end="")
				print("\\",end="")
			else:
				print(".", end="")
		# right part
		for k in range(i, SIZE):
			print(".", end="")
		print("|")


# lower part
def lower():
	# print SIZE line "|"
	for i in range(1, SIZE + 1):
		print("|", end="")
		# separate two for loop
		# left part
		for j in range(-SIZE+i, i):
			if j > 0:
				print(".", end="")
		# right part
		for k in range(-SIZE+i, i):
			# judge when to print '\/'
			if k < 1:
				print("\\", end="")
				print("/", end="")
			else:
				print(".", end="")
		print("|")


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()