# smallest unit is 8x8 which is smaller than a bullet
# so we only need to store 100x75 arrays 
level_array = []
def write_file(name):
	level = open(name,w)#remember to include .txt
	for i in level_array:
		level.write(str(i)+"\n")
	for i in range(30):
		level.write(str())
def line_add(lst):
	level_array.append(lst)
def from_file(name):
	level = open(name,w)
	level_array = []
	line = level.readline()
	while line != "\n":
		temp = []
		for i in line:
			if i not(in ", []"):
				temp.append(i)
		level_array.append(temp)
		line = level.readline()