morse_code = {
    "A" : ".-", 
    "B" : "-...", 
    "C" : "-.-.", 
    "D" : "-..", 
    "E" : ".", 
    "F" : "..-.", 
    "G" : "--.", 
    "H" : "....", 
    "I" : "..", 
    "J" : ".---", 
    "K" : "-.-", 
    "L" : ".-..", 
    "M" : "--", 
    "N" : "-.", 
    "O" : "---", 
    "P" : ".--.", 
    "Q" : "--.-", 
    "R" : ".-.", 
    "S" : "...", 
    "T" : "-", 
    "U" : "..-", 
    "V" : "...-", 
    "W" : ".--", 
    "X" : "-..-", 
    "Y" : "-.--", 
    "Z" : "--.."
}

def encode_morze(phrase):
	signal = { "." : "^", "-" : "^^^" }
	pause = { "element" : "_", "char" : "___", "word" : "____" }
	punctuation = ['.', ',', ':', ';', '!', '?']
	for char in punctuation:
		phrase = phrase.replace(char, '')
	phrase = phrase.replace('  ', ' ')
	encoded = ''
	while len(phrase) > 0:
		# intercept whitespace
		if phrase[0] == ' ':
			encoded = encoded + pause["word"]
		elif not phrase[0].isalpha():
			# SKIP THE DIGITS and PUNCTUATION
			encoded = encoded
		else:
			_char = morse_code[phrase[0].upper()]
			while len(_char) > 0:
				encoded = encoded + signal[_char[0]]
				if len(_char) > 1 :
					encoded = encoded + pause['element']
				_char = _char[1:]
			if len(phrase) > 1:
				encoded = encoded + pause['char']
		phrase = phrase[1:]
	return encoded

print encode_morze("HOUSTON WE HAVE A PROBLEM!")
print encode_morze("HOUSTON WE HAVE A PROBLEM")

exit()