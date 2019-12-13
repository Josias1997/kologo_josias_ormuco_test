# Question A: Your goal for this question is to write a program that accepts two lines 
# (x1,x2) and (x3,x4) on the x-axis and returns whether they overlap. As an example, (1,5) 
# and (2,6) overlaps but not (1,5) and (6,8).


from utils import validate_input_format, check_order
from custom_exceptions import OrderError, InvalidFormat

def test_if_overlap(first_line, second_line):
	'''
	 This function accepts two lines an return whether they overlap or not.
	 It tests if the strings format are valid and finally makes the test
	 test_if_overlap('(x1,x2)', '(x3,x4)')
	'''
	try:
		if validate_input_format(first_line) and validate_input_format(second_line):
			first_x_values = [int(x) for x in str(first_line[1:len(first_line) - 1]).split(',')]
			second_x_values = [int(x) for x in str(second_line[1:len(second_line) - 1]).split(',')]

			if check_order(first_x_values, second_x_values):
				if first_x_values[0] <= second_x_values[1] and first_x_values[1] >= second_x_values[0]:
					return True
				else:
					return False
			else:
				raise OrderError
		else:
			raise InvalidFormat
	except TypeError:
		return 'Invalid type'
	except OrderError:
		return 'x2 must be greater than x1'
	except InvalidFormat:
		return 'Invalid Format -> Correct format : (x1,x2)' 



