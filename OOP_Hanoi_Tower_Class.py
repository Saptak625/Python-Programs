class Tower:
	def __init__(self, n, start='a'):
		self.height=n
		self.start=start
		self.create()

	def create(self):
		list=['a','b','c']
		created_list=[[],[],[]]
		ind=list.index(self.start)
		created_list[ind]=[ self.height-x for x in range(self.height) ]
		self.display=created_list

	def move(self,start, end, n=1, classic_meth=False):
		start_i=self.quickindex(start)
		end_i=self.quickindex(end)
		if n==1:
			obj=self.display[start_i][len(self.display[start_i])-1]
			self.display[start_i].remove(obj)
			self.display[end_i].append(obj)
			if classic_meth==True:
				print(str(self.display))
			else:
				print(self.smart_display())
				print("")
		elif n>1: 
			self.solve(start, end, n, classic_meth)
		else:
			return "N value must be a positive integer."

	def solve(self, start='a', end='c', n=None, classic_meth=False):
		list=['a','b','c']
		#Solve problem recursively
		if start.lower() not in list:
			return 'Start is invalid.'
		else: 
			list.remove(start)
		if end.lower() not in list:
			return 'End is invalid.'
		else: 
			list.remove(end)
		other=list[0]
		if n==None:
			n=self.height
		#Recursive Solving Algorithm
		if n==1:
			self.move(start, end, n, classic_meth)
		else:
			self.move(start, other, n-1, classic_meth)
			self.move(start, end, 1, classic_meth)
			self.move(other, end, n-1, classic_meth)

	def smart_display(self, start=None, end=None, step=None):
		if start==None and end==None:
			return f"A: {self.display[0]} \nB: {self.display[1]} \nC: {self.display[2]}"
	def reset(self):
		self.create()

	def __repr__(self):
		return str(self.display)

	def __str__(self):
		return str(self.smart_display())

	@staticmethod
	def quickindex(str):
		list=['a','b','c']
		return list.index(str)

tower_1=Tower(10)
print(tower_1)
tower_1.solve()
