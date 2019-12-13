import unittest
from main import test_equality

class EqualityTest(unittest.TestCase):
	
	def test_greater_than(self):
		self.assertEqual(test_equality("1.3", "1"), '{0} is greater than {1}'.format("1.3", "1"))
		self.assertEqual(test_equality("6", "4"), '{0} is greater than {1}'.format("6", "4"))
		self.assertEqual(test_equality("2.567", "2.5"), '{0} is greater than {1}'.format("2.567", "2.5"))
		self.assertEqual(test_equality("4.66", "4.4"), '{0} is greater than {1}'.format("4.66", "4.4"))

	def test_less_than(self):	
		self.assertEqual(test_equality("1", "1.3"), '{1} is less than {0}'.format("1.3", "1"))
		self.assertEqual(test_equality("4", "6"), '{1} is less than {0}'.format("6", "4"))
		self.assertEqual(test_equality("2.5", "2.567"), '{1} is less than {0}'.format("2.567", "2.5"))
		self.assertEqual(test_equality("4.4", "4.66"), '{1} is less than {0}'.format("4.66", "4.4"))


	def test_equal_to(self):	
		self.assertEqual(test_equality("1", "1"), '{1} is equal to {0}'.format("1", "1"))
		self.assertEqual(test_equality("4", "4"), '{1} is equal to {0}'.format("4", "4"))
		self.assertEqual(test_equality("2.567", "2.567"), '{1} is equal to {0}'.format("2.567", "2.567"))
		self.assertEqual(test_equality("4.4", "4.4"), '{1} is equal to {0}'.format("4.4", "4.4"))

	def test_validate_input_type(self):
		self.assertEqual(test_equality("èhsjhdjs", "1"), 'Non-numeric string')
		self.assertEqual(test_equality("king", "king"), 'Non-numeric string')


if __name__ == '__main__':
	unittest.main()