class Graph(): 
	def __init__(self, vertices): 
		self.V = vertices #Number of vertices
		self.graph=[[0 for column in range(vertices)]for row in range(vertices)] #Storing graph values as 0

	# Function to check if the current color assignment is safe for vertex v 
	def isSafe(self,v,colour,c): 
		for i in range(self.V): 
			if self.graph[v][i]==1 and colour[i]==c: 
				return False
		return True
	
	# Recursive function to solve graph coloring problem 
	def graphColourUtil(self,m,colour,v): 
		if v==self.V: 
			return True
		for c in range(1, m+1): 
			if self.isSafe(v,colour,c)==True: 
				colour[v]=c 
				if self.graphColourUtil(m,colour,v+1)==True: 
					return True
				colour[v]=0

	def graphColouring(self, m): 
		colour=[0]*self.V 
		if self.graphColourUtil(m,colour,0)==None:
			return False
		# Solution 
		print("Chromatic number : ",m)
		print("Coloring Sequence :",*colour)
		return True

n=int(input("Enter number of nodes : "))
input_string=input("Enter the node values according to their connectivity with corresponding nodes : ")
list=input_string.split()
k=0
matrix=[]
for i in range(0,n):
    matrix.append([])
    for j in range(0,n):
        matrix[i].append(0)
        matrix[i][j]=int(list[k])
        k=k+1
g=Graph(n) 
g.graph=matrix 
for i in range(n):
	if g.graphColouring(i) is True:
		break
	 

