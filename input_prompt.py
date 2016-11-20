def input_prompt(msg):
	try:
		return raw_input(msg)
	except NameError:
		return input(msg)