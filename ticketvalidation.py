import datetime
# ask user how many tickets you wanna buy
ask_tickets = input('How many tickets do you to purchase: ')

# Your ticket is valid until 2020-05-12 and the total price 60000
if len(ask_tickets) > 0:
    total_tickets = int(ask_tickets)
    # info: 1 ticket valid for 1 week
    ticket_valid = 7
    # info: ticket is 15000
    ticket_price = 15000
    today = datetime.datetime.today()
    delta = datetime.timedelta(days=ticket_valid*total_tickets)
    expired_date = today + delta
    total_price = ticket_price * total_tickets
    print("You ticket valid until {0} and total price is {1}".format(expired_date.date(), total_price))
else:
    print("You haven't purchased anything")
    ask_tickets = input('How many tickets do you to purchase: ')

