import math

#Sigmoid function
def sigm(x, m):
	return (1 + math.erf(x - m)) / 2

class top_node():

	#Intializes all variables
	def __init__(self):
		self.val = 0

	#Sets the value of val
	def ch_val(self, new_val):
		self.val = new_val

	#Returns the value that the node is given
	def value(self):
		print(self.val)
		return self.val


class node:
	
	#Initializes all the variables
	def __init__(self, m):
		self.parents = []
		self.m = m

	#Makes you able to add a parent to the node
	def add_parent(self, parent, factor):
		self.parents.append([parent, factor])
	#Summarizes the parentnodes with the factors and returns the sigmoid result
	def value(self):
		tot_val = 0
		for parent in self.parents:
			tot_val += parent[1] * parent[0].value()
		return sigm(tot_val, self.m)