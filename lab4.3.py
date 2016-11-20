import sys

text = sys.argv[1]

p_open = "("
p_close = ")"
flag = True
counter = 0

char_index = 0
while char_index < len(text):
	if text[char_index] == p_open:
		counter = counter + 1
		flag = False
	elif text[char_index] == p_close:
		counter = counter - 1
	if counter < 0:
		flag = False
		break
	elif counter == 0:
		flag = True
	char_index = char_index + 1

if flag:
	print "YES"
else:
	print "NO"

exit()