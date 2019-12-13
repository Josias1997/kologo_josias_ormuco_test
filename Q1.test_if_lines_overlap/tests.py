import unittest
from main import test_if_overlap

class OverlapTest(unittest.TestCase):
	'''
		Overlap function test cases
	'''
	def test_positive_values(self):
		self.assertEqual(test_if_overlap('(1,5)', '(2,6)'), True)
		self.assertEqual(test_if_overlap('(1,5)', '(6,8)'), False)
		self.assertEqual(test_if_overlap('(2,6)', '(1,5)'), True)
		self.assertEqual(test_if_overlap('(6,8)', '(1,5)'), False)

	def test_negative_values(self):
		self.assertEqual(test_if_overlap('(-5,-1)', '(-6,-2)'), True)
		self.assertEqual(test_if_overlap('(-5,-1)', '(-8,-6)'), False)
		self.assertEqual(test_if_overlap('(-6,-2)', '(-5,-1)'), True)
		self.assertEqual(test_if_overlap('(-8,-6)', '(-5,-1)'), False)

	def test_values_order(self):
		self.assertEqual(test_if_overlap('(-1,-5)', '(-6,-2)'), 'x2 must be greater than x1')

	def test_validate_format(self):
		self.assertEqual(test_if_overlap('1,3', '(6,7)'), 'Invalid Format -> Correct format : (x1,x2)')
		self.assertEqual(test_if_overlap('3','6'), 'Invalid Format -> Correct format : (x1,x2)')

	def test_validate_input_type(self):
		self.assertEqual(test_if_overlap(True, '(6,7)'), 'Invalid type')
		self.assertEqual(test_if_overlap(3,10), 'Invalid type')


if __name__ == '__main__':
	unittest.main()