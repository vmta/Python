import sys

list = sys.argv[1:]

rev_text = ''
i = len(list) - 1
while i >= 0:
	rev_text = rev_text + list[i]
	if i != 0:
		rev_text = rev_text + ' '
	i = i - 1

print rev_text

exit()
