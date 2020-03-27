import sys
# sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList, ListNode



class Queue:
	def __init__(self):
		# dll = DoublyLinkedList()
		self.dll = DoublyLinkedList()

		self.size = 0
		# Why is our DLL a good choice to store our elements?
		# self.storage = ?

	def enqueue(self, value):
		self.dll.add_to_tail(value)
		# print(15, value, self.len())
		
	def dequeue(self):
		j = self.dll.remove_from_head()
		# print(19, j)
		return j

	def len(self):
		return self.dll.__len__()
		
# f = Queue()
# f.enqueue(4)
# print(f.len())
# f.enqueue(6)
# print(f.len()) 