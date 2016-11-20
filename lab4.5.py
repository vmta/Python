import sys

key = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

template = "Welcome to the Hotel California Such a lovely place Such a lovely place"

def removeChar(msg, ch):
	i = 0
	txt = ''
	while i < len(msg):
		if msg[i] != ch:
			txt = txt + msg[i]
		i = i + 1
	return txt

def encode(msg):
	i = 0
	txt = ''
	while i < len(msg):
		pos = alphabet.find(msg[i])
		txt = txt + key[pos:pos+5] #+ ' '
		i = i + 1
	return txt

def transcode(msg):
	tmp = removeChar(template, " ")
	#i = 0
	#t = ''
	#while i < len(tmp):
	#	t = t + tmp[i]
	#	if i > 0 and (i+1)%5 == 0:
	#		t = t + ' '
	#	i = i + 1
	i = 0
	t = ''
	while i < len(msg):
		if template[i] == ' ':
			t = t + ' '
		if msg[i] == 'a':
			t = t + tmp[i].lower()
		elif msg[i] == 'b':
			t = t + tmp[i].upper()
		i = i + 1
	return t

def decode(msg):
	msg = removeChar(msg, ' ')
	msg = msg[0:len(msg)-len(msg)%5]
	
	i = 0
	t = ''
	while i < len(msg):
		if msg[i].isupper():
			t = t + 'b'
		elif msg[i].islower():
			t = t + 'a'
		i = i + 1
	
	i = 0
	msg = ''
	while i < len(t):
		pos = key.find(t[i:i+5])
		msg = msg + alphabet[pos]
		i = i + 5
	
	return msg

msg = sys.argv[1]
#act = sys.argv[2]

#if act == 'encode':
#	print transcode(encode(removeChar(msg, " ")))
#elif act == 'decode':
print decode(msg)

exit()