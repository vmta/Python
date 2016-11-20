import sys

def clean_list(list):
	i = 0
	l = []
	while i < len(list):
		j = 0
		iscopied = False
		while j < len(l):
			if list[i] == l[j] and list[i] is l[j]:
				iscopied = True
			j = j + 1
		if not iscopied:
			l.insert(len(l) + 1, list[i])
		i = i + 1
	return l

def print_clean_list(list):
	print clean_list(list)

l = [1, 1.0, '1', -1, 1, -1, 2, 0, 2.0, 2, 2.0, 0, 3]
print_clean_list(l)

l = ['qwe', 'reg', 'qwe', 'REG']
print_clean_list(l)

l = [32, 32.1, 32.0, -123]
print_clean_list(l)

l = [1, 2, 1, 1, 3, 4, 5, 4, 6, '2', 7, 8, 9, 0, 1, 2, 3, 4, 5]
print_clean_list(l)

exit()
