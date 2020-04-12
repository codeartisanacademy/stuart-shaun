import datetime

# delta a difference between time
one_week = datetime.timedelta(weeks=1)
two_weeks = datetime.timedelta(weeks=2)
five_days = datetime.timedelta(days=5)

expired_in = 30
today = datetime.date.today()
expiration_date = today + datetime.timedelta(days=expired_in)

print("A week from now is {0}".format(today+one_week))
print("Two weeks from now is {0}".format(today+two_weeks))
print("5 days from now is {0}".format(today+five_days))
print("Your ticket will be expired at {0}".format(expiration_date))
