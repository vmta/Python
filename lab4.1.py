import sys

def text_prompt(msg):
	try:
		return raw_input(msg)
	except NameError:
		return input(msg)

def clean(text):
	clean_text = ''
	i = 0
	while i < len(text):
		if text[i] != ' ':
			clean_text = clean_text + text[i]
		i = i + 1
	return clean_text

def check(msg):
	clean_text = clean(msg)
	flag = True
	i = 0
	while i < len(clean_text):
		if clean_text[i] != clean_text[((len(clean_text) - 1) - i)]:
			flag = False
			break
		i = i + 1
	return flag

text = ''
if len(sys.argv) < 2:
	while len(text) < 1:
		text = str(text_prompt('Expecting to receive an input : ')).lower()
else:
	text = str(sys.argv[1]).lower()

if check(text):
	print "YES"
else:
	print "NO"

exit()
