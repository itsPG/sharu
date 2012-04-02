import sys
class num_checker :
	data = set()
	def clear(self) :
		self.data = set()
	def add_and_chk(self, q) :
		if q == 0 :
			return True
		q = q - 1
		if q in self.data :
			return False
		else :
			self.data.add(q)
			return True
#======================================================================================

class sudoku :
	data = []
	list_x = []
	list_y = []
	list_size = 0
	flag_solved = False
	solution_count = 0
	max_depth = 0
	def init(self) :
		self.data = []
		for i in range(0, 9) :
			self.data.append([])
			for j in range(0, 9) :
				self.data[i].append(0)

	#--------------------------------------------------------------------------------
	def read_file(self, filename) :
		self.init()
		fin = open(filename, "r")
		tmp = 0
		for i in range(0, 9) :
			for j in range(0, 9) :

				while 1 :
					tmp = fin.read(1)
					if not tmp :
						print("read file error at %d %d" % (int(i), int(j)))
						return 0
					if tmp > '9' or tmp < '0' :
						continue
					else :
						break
				self.data[i][j] = int(tmp)
	#--------------------------------------------------------------------------------
	def chk(self) :
		for i in range(0, 9) :

			flag = set()
			for j in range(0, 9) :
				tmp = self.data[i][j] - 1
				if tmp == -1 :
					continue
				if tmp not in flag :
					flag.add(tmp)
				else :
					return False

			flag = set()
			for j in range(0, 9) :
				tmp = self.data[j][i] - 1
				if tmp == -1 :
					continue
				if tmp not in flag :
					flag.add(tmp)
				else :
						return False

		for i in range(0, 9, 3) :
			for j in range(0, 9, 3) :
				flag = set()
				for ii in range(i, i + 3) :
					for jj in range(j, j + 3) :
						tmp = self.data[jj][ii] - 1
						if tmp == -1 :
							continue
						if tmp not in flag :
							flag.add(tmp)
						else :
							return False
		return True
	#--------------------------------------------------------------------------------
	def chk2(self, in_x, in_y) :

		row_flag = num_checker()
		row_flag.clear()
		column_flag = num_checker()
		column_flag.clear()
		for i in range(0, 9) :
			if not row_flag.add_and_chk(self.data[in_y][i]) :
				return False
			if not column_flag.add_and_chk(self.data[i][in_x]) :
				return False

		grid_flag = num_checker()
		grid_flag.clear()
		s_x = in_x - in_x % 3
		s_y = in_y - in_y % 3
		for i in range(s_y, s_y + 3) :
			for j in range(s_x, s_x + 3) :
				if not grid_flag.add_and_chk(self.data[i][j]) :
					return False

		return True
	#--------------------------------------------------------------------------------
	def show(self) :
		for i in range(0, 9) :
			for j in range(0, 9) :
				sys.stdout.write("%d " % int(self.data[i][j]))
			print(" ")
	#--------------------------------------------------------------------------------

	def push_list(self, inx, iny) :
		self.list_x.append(inx)
		self.list_y.append(iny)
	#--------------------------------------------------------------------------------
	def create_list(self) :
		self.list_x = [-1]
		self.list_y = [-1]
		list_size = 0
		for i in range(0, 9) :
			for j in range(0, 9) :
				if self.data[i][j] == 0 :
					self.push_list(j, i)
					self.list_size = self.list_size + 1
	#--------------------------------------------------------------------------------
	def DFS(self, depth, num) :
		if depth > self.max_depth :
			self.max_depth = depth
		if self.solution_count > 100 :
			print("More than 100 solutions.")
			return 
		tx = self.list_x[depth]
		ty = self.list_y[depth]
		self.data[ty][tx] = num

		#if not self.chk() :
		if not self.chk2(tx, ty) :
			self.data[ty][tx] = 0
			return 

		if depth == self.list_size :
			self.solution_count += 1
			print("####    solution #%d    ####" % self.solution_count)
			self.show()
			print("###########################################")
			self.flag_solved = True
			
			return 

		for i in range(1, 10) :
			self.DFS(depth + 1, i)

		self.data[ty][tx] = 0
		return 
	#--------------------------------------------------------------------------------
	def go(self) :
		for i in range(1, 10) :
			self.DFS(1, i)
		if self.flag_solved :
			print("max depth %d " % self.max_depth)
			print("Solutions count : %d" % self.solution_count)
		else :
			print("No Solution")
	#--------------------------------------------------------------------------------
#======================================================================================

rixia = sudoku()
rixia.init()
filename = raw_input("Enter a filename : ")
rixia.read_file(filename)
rixia.create_list()
rixia.go()