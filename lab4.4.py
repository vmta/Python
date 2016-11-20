import sys

ticket_a = int(sys.argv[1])
ticket_b = int(sys.argv[2])

def calc(ticket):
	sum_a = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
	sum_b = int(ticket[3]) + int(ticket[4]) + int(ticket[5])
	if sum_a == sum_b:
		return 1
	else:
		return 0

sum = 0
for i in range(ticket_a, ticket_b + 1):
	ticket = str(i)
	j = len(ticket)
	if j < 6:
		while j < 6:
			ticket = '0' + ticket
			j = j + 1
	sum = sum + calc(ticket)

print sum

exit()