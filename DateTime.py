import datetime
currentDate = datetime.date.today()
#strftime allows you to specify the date format (string from time)
print (currentDate.strftime('%d %b, %Y'))
print (currentDate.strftime('%a %d %B %y'))
print (currentDate)
print (currentDate.month)
print (currentDate.year)
currentDate = datetime.date.today()
print (currentDate.strftime('Please attend our event %A, %B %d in the year %Y'))
# how to manually enter a date that will print?. use input
# userdate = input('Enter a date (mm/dd/yyyy)\n'
