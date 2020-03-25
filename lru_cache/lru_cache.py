from doubly_linked_list import DoublyLinkedList

class LRUCache:
	"""
	Our LRUCache class keeps track of
		* the max number of nodes it can hold
		* the current number of nodes it is holding
		* a doubly-linked list that holds the key-value entries in the correct order
		* as well as a storage dict that provides fast access to every node stored in the cache.
	"""
	def __init__(self, limit=10):
		self.limit = limit
		self.length = 0
		self.dll = DoublyLinkedList()
		self.store = {}

	"""
	Retrieves the value associated with the given key.
	Also needs to move the key-value pair to the end of the order such that the pair is considered most-recently used.
	
	Returns the value associated with the key or None if the key-value pair doesn't exist in the cache.
	"""
	def get(self, key):
		# print(24, key)
		if key in self.store:
			current = self.store[key]
			# print(25, current.value)

			self.dll.move_to_front(current)
			return current.value[1]

		else:
			return None


	"""
	Adds the given key-value pair to the cache.
	The newly-added pair should be considered the most-recently used entry in the cache.

	If the cache is already at max capacity	before this entry is added,
	then the oldest entry in the cache needs to be removed to make room.
	
	If key already exists in the cache,
	overwrite the old value associated with the key with the newly-specified value.
	"""
	def set(self, key, value):
		# print(47, key, value)
		if key in self.store:
			# if store item exists
			current = self.store[key]
			current.value = (key, value)
			self.dll.move_to_front(current)
			return current.value

		# if not already in the store
		# chk and prepare length first
		if self.length == self.limit:
			self.length -= 1
			del self.store[self.dll.tail.value[0]]
			self.dll.remove_from_tail()

		# NOW add to the store
		self.length += 1
		self.dll.add_to_head((key,value))
		self.store[key] = self.dll.head



f = LRUCache()

f.set('item1', 'a')
f.set('item2', 'b')
f.set('item3', 'c')
f.set('item2', 'z')

# print(f.get('item1'))
# print(f.get('item2')) 

