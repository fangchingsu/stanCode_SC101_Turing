"""
File: weather_master.py
Name: Fangching Su
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
# Constant
LEAVE = -1


def main():
	"""
	input temperatures to find the highest temperature, lowest temperature,
	average temperature, and calculate cold days
	"""
	print("stanCode \"Weather Master 4.0\"!")
	new_wx = int(input("Next Temperature: (or " + str(LEAVE) + " to quit)? "))
	# let first input temperature equal to maximum weather and minimum weather
	max_wx = new_wx
	min_wx = new_wx

	# declare variables
	save_data = 0
	count_day = 0
	cold_count = 0

	# the first input weather is equal to quit number
	if new_wx == LEAVE:
		print("No temperatures were entered.")
	else:
		while True:
			if new_wx == LEAVE:
				break
			# judge the input weather is bigger or smaller than maximum weather or minimum weather
			elif new_wx > max_wx:
				max_wx = new_wx
			elif new_wx < min_wx:
				min_wx = new_wx
			# judge the weather that is lower than 16 degree
			if new_wx < 16:
				cold_count += 1
			# plus weather temperature input together
			save_data += new_wx
			# count input times
			count_day += 1

			new_wx = int(input("Next Temerature: (or " + str(LEAVE) + " to quit)? "))

		print("Highest Temperature: "+ str(max_wx))
		print("Lowest Temperature: " + str(min_wx))
		print("Average: " + str(save_data/count_day))

		if cold_count == 1 or cold_count == 0:
			print(str(cold_count) + " cold day")
		else:
			print(str(cold_count) + " colds day")

###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
