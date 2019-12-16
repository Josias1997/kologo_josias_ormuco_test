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
# the cache can expire if a timeout is provided each time an item is used
# is timeout value is automatically reset. An item expires when he's not used 
# and it timeout is reached.

from threading import Timer, RLock
from time import time

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
        self.last_used_time = None

    def _update_last_used_time(self):
        self.last_used_time = time()

    
class LRUCache:
    def __init__(self, max_size: int, expires_at=None):
        self.max_size = max_size
        self.expires_at = expires_at
        self.cache = dict()
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.timer = None
        self.lock = RLock()

        if self.expires_at:
            self._cleanup()

    def get(self, key)
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

    def put(self, key, value) -> None:
        try:
            self.lock.acquire()
            if key in self.cache:
                self._remove(self.cache[key])
            node = Node(key, value)
            self._add(node)
            if len(self.cache) > self.max_size:
                node = self.head.next
                self._remove(node)
        finally:
            self.lock.release()
    
    def _remove(self, node) -> None:
        try: 
            self.lock.acquire()
            next = node.next
            prev = node.prev
            prev.next = next
            next.prev = prev
            del self.cache[node.key]
        finally:
            self.lock.release()

    
    def _add(self, node):
        try:
            self.lock.acquire()
            prev = self.tail.prev
            prev.next = node
            self.tail.prev = node
            node.prev = prev
            node.next = self.tail
            self.cache[node.key] = node
            node._update_last_used_time()
        finally:
            self.lock.release()

    def _cleanup(self):
        self._clear_cache_item()
        timer = Timer(self.expires_at, self._cleanup)
        timer.start()
        self.timer = timer


    def _clear_cache_item(self):
        if not len(self.cache):
            return
        try:
            self.lock.acquire()
            clear_time = time() - self.expires_at
            node = self.head.next
            while not node is self.tail and node.last_used_time < clear_time:
                self._remove(node)
                node = self.head.next
        finally:
            self.lock.release()

    def _max_size(self):
        return self.max_size


    def current_size(self):
        return len(self.keys())


    def stop_timer(self):
        self.timer.cancel()
    

    def keys(self):
        return self.cache.keys()
