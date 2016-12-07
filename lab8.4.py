def make_sudoku(size):
	def rotateRow(_list, _shift):
		return _list[_shift:] + _list[:_shift]
	def rotateCol(_list):
		for i in range(size):
			_list.insert((i + 1) * size, _list.pop(i * size))
		return _list
	sudoku = []
	preemptive = [i + 1 for i in range(size * size)]
	for row in range(size):
		currentR = rotateCol(preemptive)
		for col in range(size):
			currentC = rotateRow(currentR, col * size)
			sudoku.append(currentC)
	return sudoku

print "=== TEST START ==="

print make_sudoku(1) # [[1]]
print make_sudoku(2) # [[1,2,3,4],[3,4,1,2],[2,1,4,3],[4,3,2,1]]
print make_sudoku(3) # [[3,5,8,1,2,7,6,4,9],[6,7,4,5,8,9,3,2,1],[2,1,9,3,4,6,5,7,8],[9,8,6,7,1,4,2,5,3],[4,3,1,2,6,5,8,9,7],[7,2,5,9,3,8,1,6,4],[1,6,3,4,7,2,9,8,5],[8,9,7,6,5,1,4,3,2],[5,4,2,8,9,3,7,1,6]]

print "==== TEST END ===="

exit(0)