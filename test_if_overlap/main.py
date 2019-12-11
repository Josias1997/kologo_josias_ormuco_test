# Question A: Your goal for this question is to write a program that accepts two lines 
# (x1,x2) and (x3,x4) on the x-axis and returns whether they overlap. As an example, (1,5) 
# and (2,6) overlaps but not (1,5) and (6,8).


import re

def test_if_overlap():
	try:
		firstLine = str(input('Type first line: Format (x1,x2)\n'))
		secondLine = str(input('Type second line: Format (x2,x3)\n'))

		while not validate_input_format(firstLine) or not validate_input_format(secondLine):
			print('Invalid input format: Input must be in this format -> (x1,x2)')
			firstLine = str(input('Type first line: Format (x1,x2)\n'))
			secondLine = str(input('Type second line: Format (x2,x3)\n'))

		first_x_values = firstLine[1:len(firstLine) - 1].split(',')
		second_x_values = secondLine[1:len(secondLine) - 1].split(',')

		if first_x_values[1] >= second_x_values[0]:
			print(f'\n{firstLine} and {secondLine} overlap')
		else:
			print(f'\n{firstLine} and {secondLine} don\'t overlap')

	except TypeError:
		print('Invalid input')


def validate_input_format(input):
	return re.match(r'^\(\d{1}\,\d{1}\)$', input)
