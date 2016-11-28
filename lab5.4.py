import os



def file_search(folder, filename):
	path = []
	make_path(folder, "", path)
	for i in path:
		if filename in i[len(i) - len(filename):]:
			return i
	return False

def make_path(folder, root, paths):
	path = str(root)
	path = path + str(folder[0]) + "/"
	if len(folder) < 2:
		paths.append(path)
	else:
		for i in range(1, len(folder)):
			if isinstance(folder[i], list):
				make_path(folder[i], path, paths)
			else:
				paths.append(path + str(folder[i]))

print "path: " + str(file_search(["C:"], "crack.exe"))

print "path: " + file_search(["C:", "1.txt", "2.txt", "3.txt", "4.txt"], "1.txt")


filename = "lab5.4.py"
folder = ["~", ["Documents", ["Education", ["workspace_python", filename]]]]
print "path: " + file_search(folder, filename)

exit()
