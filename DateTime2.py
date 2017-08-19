import datetime
userinput = input('Please enter your birthday (dd/mm/yyyy)\n')
birthday = datetime.datetime.strptime(userinput, '%d/%m/%Y').date()  #strptime is used for time #.date() tells it to only print the date and not include time
print(birthday)

currentDate = datetime.date.today() 
days = birthday - currentDate
print(days.days) # .days removes the time so only displays the days

currentTime = datetime.datetime.now() #.time() #.time will only print the time and not the date
print (currentTime)
print (currentTime.hour)
print (currentTime.minute)
print (currentTime.second)
print (datetime.datetime.strftime(currentTime,'%H:%M')) # check strftime.org for all the string times available
