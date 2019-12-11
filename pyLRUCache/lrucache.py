# The cache is implemented using a combination of a python dictionary (hash
# table) and a circular doubly linked list. Items in the cache are stored in
# nodes. These nodes make up the linked list. The list is used to efficiently
# maintain the order that the items have been used in. The head of
# the list contains the least recently used item, the tail of the list
# contains the most recently used item. When an item is used it can easily
# (in a constant amount of time) be moved to the back of the list, thus
# updating its position in the ordering. These nodes are also placed in the
# hash table under their associated key. The hash table allows efficient
# lookup of values by key.

from threading import Timer, RLock
from time import time

class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
        self.last_used_time = None

    def _update_last_used_time(self):
        self.last_used_time = time()

    
class LRUCache:
    def __init__(self, size: int, expires=None):
        self.size = size
        self.expires = expires
        self.cache = dict()
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.timer = None
        self.lock = RLock()

        if self.expires:
            self._cleanup()

    def get(self, key: int) -> int:
        try:
            self.lock.acquire()
            if key in self.cache:
                node = self.cache[key]
                self._remove(node)
                self._add(node)
                return node.value
            return -1
        finally:
            self.lock.release()

    def put(self, key: int, value: int) -> None:
        try:
            self.lock.aquire()
            if key in self.cache:
                self._remove(self.cache[key])
            node = Node(key, value)
            self._add(node)
            self.cache[key] = node
            if len(self.cache) > self.size:
                node = self.head.next
                self._remove(node)
                del self.cache[node.key]
        finally:
            self.lock.release()
    
    def _remove(self, node) -> None:
        next = node.next
        prev = node.prev
        prev.next = next
        next.prev = prev
    
    def _add(self, node):
        try:
            self.lock.acquire()
            prev = self.tail.prev
            prev.next = node
            self.tail.prev = node
            node.prev = prev
            node.next = self.tail
            node._update_last_used_time()
        finally:
            self.lock.release()

    def _cleanup(self):
        self._clear_cache_item()
        timer = Timer(self.expires, self._cleanup)
        timer.start()
        self.timer = timer


    def _clear_cache_item(self):
        if not len(self.cache):
            return
        try:
            self.lock.acquire()
            clear_time = time() - self.expires
            node = head.next
            while not node is self.tail and node.last_used_time < clear_time:
                self._remove(node)
        finally:
            self.lock.release()

