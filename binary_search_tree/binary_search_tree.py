import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	# Insert the given value into the tree
	def insert(self, incoming):
		# print(25,self.value)
		if not self.value:
			self.value = incoming
		else:
			if incoming < self.value:
				# print("left")
				if self.left == None:
					self.left = BinarySearchTree(incoming)
				else: 
					self.left.insert(incoming)
			elif incoming >= self.value:
				# print("right")
				if self.right == None:
					self.right = BinarySearchTree(incoming)
				else:
					self.right.insert(incoming)

	# Return True if the tree contains the value
	# False if it does not
	def contains(self, target):
		if self.value is None:
			print(36, False, target, end="\n\n")
			return False
		elif self.value == target:
			print(39, True, target, end="\n\n")
			return True
		else:
			if target < self.value:
				print("left at", self.value)
				if self.left:
					self.left.contains(target)
				else:
					print(47, False, target, end="\n\n")
					return False
			else:
				print("right at", self.value)
				if self.right:
					self.right.contains(target)
				else:
					print(54, False, target, end="\n\n")
					return False


	# Return the maximum value found in the tree
	def get_max(self):
		pass

	# Call the function `cb` on the value of each node
	# You may use a recursive or iterative approach
	def for_each(self, cb):
		pass

	# DAY 2 Project -----------------------

	# Print all the values in order from low to high
	# Hint:  Use a recursive, depth first traversal
	def in_order_print(self, node):
		pass

	# Print the value of every node, starting with the given node,
	# in an iterative breadth first traversal
	def bft_print(self, node):
		pass

	# Print the value of every node, starting with the given node,
	# in an iterative depth first traversal
	def dft_print(self, node):
		pass

	# STRETCH Goals -------------------------
	# Note: Research may be required

	# Print Pre-order recursive DFT
	def pre_order_dft(self, node):
		pass

	# Print Post-order recursive DFT
	def post_order_dft(self, node):
		pass

f = BinarySearchTree(5)

f.insert(2)
f.insert(3)
f.insert(7)
f.insert(6)
f.insert(12)
f.insert(17)
f.insert(21)
# f.insert(22)
f.insert(45)
f.insert(46)
f.insert(19)
f.insert(28)

# print(f.contains(17))
# print(f.contains(28))
f.contains(2)
f.contains(3)
f.contains(8)
f.contains(27)
# print(f.contains(46))