# Question B
# The goal of this question is to write a software library that accepts 2 version 
# string as input and returns whether one is greater than, equal, or less than the other. 
# As an example: “1.2” is greater than “1.1”. Please provide all test cases you could think of.



from decimal import Decimal, InvalidOperation

def test_equality(first_string, second_string):
	try:
		if Decimal(first_string) > Decimal(second_string):
			return f'{first_string} is greater than {second_string}'
		elif Decimal(first_string) < Decimal(second_string):
			return f'{first_string} is less than {second_string}'
		else:
			return f'{first_string} is equal to {second_string}'
	except InvalidOperation:
		return 'Non-numeric string'
