# Created by Roman Beya
# Created for ICS3U
# Created on 6-Nov-2017
# This program calculates the middle percentage of the level inputted by the user

def get_grades():
	# This function will calculate the 'middle' grade of the mark inputted
	
	# get user input
	grades = raw_input("Enter your grade: ")
	
	# hard code all grade levels
	if grades == '4+':
		level_four_plus = (95 + 100) / 2
		return level_four_plus
		
	elif grades == '4':
		level_four = (87 + 94) / 2
		return level_four
		
	elif grades == '4-':
		level_four_minus = (80 + 86) / 2
		return level_four_minus
		
	elif grades == '3+':
		level_three_plus = (77 + 79) / 2
		return level_three_plus
		
	elif grades == '3':
		level_three = (73 + 76) / 2
		return level_three
	
	elif grades == '3-':
		level_three_minus = (70 + 72) / 2
		return level_three_minus
	
	elif grades == '2+':
		level_two_plus = (67 + 69) / 2
		return level_two_plus
		
	elif grades == '2':
		level_two = (63 + 66) / 2
		return level_two
	
	elif grades == '2-':
		level_two_minus = (60 + 62) / 2
		return level_two_minus
		
	elif grades == '1+':
		level_one_plus = (57 + 59) / 2
		return level_one_plus
		
	elif grades == '1':
		level_one = (53 + 56) / 2
		return level_one
	
	elif grades == '1-':
		level_one_minus = (50 + 52) / 2
		return level_one_minus
		
	elif grades == 'R':
		level_R = (0 + 49) / 2
		return level_R
		
	elif grades == 'NE':
		level_Zero = 0
		return level_Zero
	
	# Using a condition to test whether or not the program has ended
	elif grades == '-1':
		return -1
			
grade = get_grades()
print grade
		
