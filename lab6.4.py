def find_most_frequent(text):
	
	# Set text to lowercase
	text = text.lower()
	
	# Define punctuation characters to be removed
	puncts = ",.:;!?-"
	
	# Replace all punctuation characters with whitespace
	for punct in puncts:
		text = text.replace(punct, " ")
	
	# Split text by words with whitespace as delimiter
	text = text.split()
	
	# This one is tricky:
	#   for each unique word in set(text) - (set stores only unique values) 
	#   count occurrences of word in text
	#   and store in a matrix, where first column is word
	#   and second column is occurrences of that word in text
	s = [[word, text.count(word)] for word in set(text)]
	
	# Define how much frequent is the frequent word
	maxVal = 0
	#maxIndex = 0
	for index in range(len(s)):
		if s[index][1] > maxVal:
			maxVal = s[index][1]
			#maxIndex = index
	
	# Build a list of most frequently used word(s)
	frequentWords = []
	for index in range(len(s)):
		if s[index][1] == maxVal:
			frequentWords.append(s[index][0])
	
	return frequentWords
	#return s[maxIndex][0] + " occurred " + str(s[maxIndex][1]) + " times"


sample1 = 'Hello,Hello, my dear!'
sample2 = 'to understand recursion you need first to understand recursion...'
sample3 = 'Mom! Mom! Are you sleeping?!!!'
sample4 = "Zootopia is the funny Cartoon. I haven't seen such a cartoons in a long run."

samples = [sample1, sample2, sample3, sample4]

for sample in samples:
	print sample
	print find_most_frequent(sample)

exit()