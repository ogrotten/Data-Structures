import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
	def __init__(self):
		# self.size = 0
		# Why is our DLL a good choice to store our elements?
		self.dll = DoublyLinkedList()

	def push(self, value):
		return self.dll.add_to_tail(value)

	def pop(self):
		return self.dll.remove_from_tail()

	def len(self):
		return self.dll.__len__()

# f = Stack()
# f.push(4)
# print(f.len())
# f.push(6)
# print(f.len()) 
# print(f.pop())
# print(f.len()) 