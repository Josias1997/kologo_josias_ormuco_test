import unittest
from lrucache import LRUCache
import time 
from threading import Timer, RLock

class LRUTest(unittest.TestCase):
	def test_instanciation_without_timeout(self):
		cache = LRUCache(5)
		cache.put('1', '2')
		cache.put('2', '3')
		cache.put('3', '4')
		cache.put('4', '5')
		cache.put('first', 'value')
		self.assertEqual(cache.get('1'), '2')
		self.assertEqual(cache.get('2'), '3')
		self.assertEqual(cache.get('3'), '4')
		self.assertEqual(cache.get('4'), '5')
		self.assertEqual(cache.get('5'), -1)


	def test_instanciation_with_timeout_1sec(self):
		cache = LRUCache(5, 1)
		cache.put('first', 'first')
		cache.put('second', 'second')
		self.assertEqual(len(cache.keys()), 2)
		time.sleep(2)
		self.assertEqual(len(cache.keys()), 0)
		cache.stop_timer()

	def test_instanciation_with_timeout_5sec(self):
		cache = LRUCache(5, 5)
		cache.put('first', 'first')
		cache.put('second', 'second')
		self.assertEqual(len(cache.keys()), 2)
		time.sleep(7)
		self.assertEqual(len(cache.keys()), 0)
		cache.stop_timer()

if __name__ == '__main__':
	unittest.main()