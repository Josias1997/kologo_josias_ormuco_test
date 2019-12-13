class OrderError(Exception):
	'''
		Raised when for a given string (x1,x2) x1 is greater than x2
	'''
	pass


class InvalidFormat(Exception):
	'''
	 Raised when the input format is different from (x1,x2)
	'''
	pass