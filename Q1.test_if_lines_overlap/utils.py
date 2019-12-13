import re

def validate_input_format(input):
	'''
		A regex that validate input format for negative values and positive values
		An exemple (4,5) (-4,-5) (4,-5), (-4, 5) ... 
		the function will return trur for those values
	'''
	return re.match(r'^\((\-)?\d{1,}\,(\-)?\d{1,}\)$', input)


def check_order(first_values, second_values):
	'''
		This function checks if axis are ordered correctly. 
		For example if we have (x1,x2) x2 must be greater or equal to x1
	'''
	return first_values[1] >= first_values[0] and second_values[1] >= second_values[0]