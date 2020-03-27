# Understanding
# 	* can we count 
# 		solution: build count var
# 	* ONE pass, not FIRST pass
# 		sol: setup for the one pass
# turns out ^^^ was incorrect :grin:
	
# 									c
# 	[h/1] [2] [3] [4] [5] [6] [7] [t/8]
# 					m

# m = c // 2 + 1

# when (count reaches tail || next == null)
# 	return m

# class Node:
# 	def __init__(self, value):
# 		self.value = value
# 		self.next = None
	
# 	def __len__(self):
# 		# come back here later
# 		return self.length

# 	def findMiddle(self, value):
# 		count = 0
# 		middle = 0

# 		while self.next != None:
# 			# track current node
# 			count += 1
# 			middle = (count // 2) + 1

# 		return middle

# f = Node(8)
# print(f.findMiddle) 






# How do you reverse a singly linked list without recursion?
# You may not store the list, or it’s values, in another data structure.

# track original tail
# make current head into tail
# increment the list, moving each next to head
# stop if current head = original tail
# 						!
# 	[h/1] [2] [3] [4] [5] [6] [7] [t/8]
# 	[h/5] [4] [3] [2] t

# 			!
# 	[h/1] [2] [3] [4] [5] [6] [7] [t/8]
# 	[h/2] [1] [3] [4] [5] [6] [7] [t/8]
# 	[h/3] [2] [1] [4] [5] [6] [7] [t/8]
# 	[h/7] [6] [5] [4] [3] [2] [1] [t/8]
# 	[h/7] [6] [5] [4] [3] [2] [1] [t/8]

# when you get to the original tail, make orig tail current head and current head to next


class Shoe():
	def __init__(self, node=None):
		# self.value = value
		self.next = None
		self.head = node
		self.tail = node

	def walk():
		# var for current_tail
		# var for original_tail
		current_head = self.head
		original_head = self.head
		original_tail = self.tail

		while self.next != original_tail
			# make current_node the new_head
