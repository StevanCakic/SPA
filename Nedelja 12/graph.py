class Graph:
	def __init__(self, num_nodes):
		self.adjacency_matrix = [] # 2D list
		for i in range(num_nodes): 
			self.adjacency_matrix.append([0 for i in range(num_nodes)])
		self.num_nodes = num_nodes

	def add_edge(self, start, end):
		self.adjacency_matrix[start][end] = 1

	def remove_edge(self, start, end):
		if self.adjacency_matrix[start][end] == 0:
			print("There is no edge between %d and %d" % (start, end))
		else:
			self.adjacency_matrix[start][end] = 0

	def contains_edge(self, start, end):
		if self.adjacency_matrix[start][end] > 0:
			return True
		else:
			return False

	def __len__(self):
		return self.num_nodes

graph1 = Graph(4)     # Create an instance of the graph with 4 nodes
graph1.add_edge(0, 1) # The 0th element is A. The 1st element is B

print(graph1.adjacency_matrix)