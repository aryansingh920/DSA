class Node:
	def __init__(self,data):
		self.data = data
		self.next = None


class LinkedList():
	def __init__(self):
		self.head = None

	def insertAtBegin(self,data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = None

	def insertAtEnd(self,data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			return

		current_node = self.head 
		while current_node.next:
			current_node = current_node.next

		current_node.next = new_node


	def removeFirstNode(self):
		if self.head is None:
			return

		self.head = self.head.next

	def printList(self):
		if self.head is None:
			print("Empty List")
		else:
			current_node = self.head
			while current_node:
				print(f"{current_node.data} -> ")
				current_node = current_node.next
		