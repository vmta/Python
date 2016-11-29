from datetime import date

def create_calendar_page(month = None, year = None):
	# First, check if any parameters are missing
	if month is None:
		month = date.today().month
	else:
		month = int(month)
	if year is None:
		year = date.today().year
	else:
		year = int(year)
	
	# Now that there are both month and year
	# construct date object
	calDate = date(year, month, 1)
	
	# Get weekday number of the first day of the given month/year
	calWeekday = calDate.isoweekday()
	
	# Get length of the given month
	monthDays = 30
	if month == 12:
		monthDays = date(year + 1, 1, 1) - calDate
	else:
		monthDays = date(year, month + 1, 1) - calDate
	
	# Construct the header
	header_1 = "--------------------"
	header_2 = "MO TU WE TH FR SA SU"
	header = "{0}\n{1}\n{2}".format(header_1, header_2, header_1)
	
	# Define body and spacer
	body = ""
	spacer = "  "
	
	# Build spaces as needed
	for day in range(1, calWeekday):
		body = "{0}{1} ".format(body, spacer)
	
	# Fill the body with day numbers
	for day in range(1, monthDays.days + 1):
		if day < 10:
			day = "0" + str(day)
		body = "{0}{1}".format(body, day)
		
		if day != monthDays.days:
			if date(year, month, int(day)).weekday() == 6:
				body = "{0}\n".format(body)
			else:
				body = "{0} ".format(body)
	
	calendar = "{0}\n{1}".format(header, body)
	
	return str(calendar)

print "===== Apr 1972 ====="
print create_calendar_page(4, 1972)

print "===== Sep 1976 ====="
print create_calendar_page(9, 1976)

print "===== Nov 2013 ====="
print create_calendar_page(11, 2013)

print "===== Jul 1983 ====="
print create_calendar_page(7, 1983)

exit()