def saddle_point(matrix):
	
	rows = len(matrix)
	cols = len(matrix[0])
	
	# Function gets rowIndex as parameter and
	# returns a minimum value in the row
	# 
	def getRowMinValue(rowIndex):
		return min(matrix[rowIndex])
	
	# Function get value and rowIndex as parameters
	# and searches for all occurrences of the value
	# in the row. If there is only one occurrence, then
	# the value is a unique minimum, otherwise return
	# False
	# 
	def isMinUnique(value, rowIndex):
		countOccurrencies = 0
		for index in range(cols):
			if matrix[rowIndex][index] == value:
				countOccurrencies = countOccurrencies + 1
		if countOccurrencies == 1:
			return True
		else:
			return False
	
	# Function gets colIndex as parameter and
	# returns a maximum value in the column
	# 
	def getColMaxValue(colIndex):
		# Assume the maximum is in the first position
		maxVal = matrix[0][colIndex]
		# Cycle through all rows and check if there
		# are numbers, greater then our assumed max
		for index in range(rows):
			if matrix[index][colIndex] > maxVal:
				maxVal = matrix[index][colIndex]
		return maxVal
	
	# Function get value and colIndex as parameters
	# and searches for all occurrences of the value
	# in the column. If there is only one occurrence,
	# then the value is a unique maximum, otherwise
	# return False
	# 
	def isMaxUnique(value, colIndex):
		countOccurrencies = 0
		for index in range(rows):
			if matrix[index][colIndex] == value:
				countOccurrencies = countOccurrencies + 1
		if countOccurrencies == 1:
			return True
		else:
			return False
	
	# Cycle through rows in order to find a saddle point
	for rowIndex in range(rows):
		
		# Get row minimum value
		rowMinValue = getRowMinValue(rowIndex)
		
		# Check if row minimum value is unique (has no dups in row)
		if isMinUnique(rowMinValue, rowIndex):
			
			# Get column maximum value
			colIndex = matrix[rowIndex].index(rowMinValue)
			colMaxValue = getColMaxValue(colIndex)
			
			# Check of row minimum value is also a column maximum
			# and column maximum value is unique (has no dups in column)
			if rowMinValue == colMaxValue and isMaxUnique(colMaxValue, colIndex):
				
				# Saddle point is found
				return (rowIndex, colIndex)
	
	# No saddle point is found
	return False



### 1

# Populate test matrix
matrix = [[13]]
print "Matrix " + str(len(matrix)) + "x" + str(len(matrix[0]))

# Display the test matrix row by row
for i in range(len(matrix)):
	print matrix[i]

# Display the saddle point coordinates
print "Saddle point coordinates: " + str(saddle_point(matrix))


### 2

# Populate test matrix
matrix = [[0,0,0],[2,1,2],[1,0,1]]
print "Matrix " + str(len(matrix)) + "x" + str(len(matrix[0]))

# Display the test matrix row by row
for i in range(len(matrix)):
	print matrix[i]

# Display the saddle point coordinates
print "Saddle point coordinates: " + str(saddle_point(matrix))


### 3

# Populate test matrix
matrix = [[1,2,3,0,1,1], [4,3,2,1,1,2], [4,3,2,0,1,1], [0,0,0,0,0,1]]
print "Matrix " + str(len(matrix)) + "x" + str(len(matrix[0]))

# Display the test matrix row by row
for i in range(len(matrix)):
	print matrix[i]

# Display the saddle point coordinates
print "Saddle point coordinates: " + str(saddle_point(matrix))


### 4

# Populate test matrix
matrix = [[5,5,5], [5,5,6], [5,4,5]]
print "Matrix " + str(len(matrix)) + "x" + str(len(matrix[0]))

# Display the test matrix row by row
for i in range(len(matrix)):
	print matrix[i]

# Display the saddle point coordinates
print "Saddle point coordinates: " + str(saddle_point(matrix))


### 5

# Populate test matrix
matrix = [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [11, 10, 9, 8, 7, 6, 5, 4, 3, 2], [12, 11, 10, 9, 8, 7, 6, 5, 4, 3], [13, 12, 11, 10, 9, 8, 7, 6, 5, 4], [14, 13, 12, 11, 10, 9, 8, 7, 6, 5], [15, 14, 13, 12, 11, 10, 9, 8, 7, 6], [16, 15, 14, 13, 12, 11, 10, 9, 8, 7], [17, 16, 15, 14, 13, 12, 11, 10, 9, 8], [18, 17, 16, 15, 14, 13, 12, 11, 10, 9], [19, 18, 17, 16, 15, 14, 13, 12, 11, 10]]
print "Matrix " + str(len(matrix)) + "x" + str(len(matrix[0]))

# Display the test matrix row by row
for i in range(len(matrix)):
	print matrix[i]

# Display the saddle point coordinates
print "Saddle point coordinates: " + str(saddle_point(matrix))

exit()