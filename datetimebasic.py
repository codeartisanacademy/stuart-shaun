import datetime

# get the object today
today = datetime.date.today()

print(today)

print("The year is {0}".format(today.year))
print("The month is {0}".format(today.month))
print("The day is {0}".format(today.day))

# the day start on Monday with index 0
print("Today is the {0}th day of the week".format(today.weekday()))

now = datetime.datetime.now();

print(now.hour)
print(now.minute)
print(now.second)

# create our own date
independece_day = datetime.date(year=1945, month=8, day=17)
print(independece_day)

lunch_time = datetime.time(hour=12, minute=30, second=0)
print(lunch_time)

# math operation in datetime
age = datetime.date.today() - independece_day
print(age.days)