players = [
    {
        'name': 'Michael Jordan',
        'team': 'Chicago Bulls'
    },
    {
        'name': 'Magic Johnson',
        'team': 'Lakers'
    },
    {
        'name': 'Lary Bird',
        'team': 'Boston Celtics'
    }
]

print(players[0]['name'])

# using for loop to print each key in the dictionary
# The goat is Michael Jordan from Chicago Bulls
# The goat is Magic Johnson from Lakers
# The goat is Lary Bird from Boston Celtics
for item in players:
    print("The goat is {0} from {1}".format(item['name'], item['team']))