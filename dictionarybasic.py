# dictionary is a key-value pair

indonesia = {
    'name': 'Republik Indonesia',
    'population': 250000000,
    'continent': 'Asia',
    'capital': 'Jakarta'
}

print(indonesia['capital'])

indonesia['language'] = 'Bahasa Indonesia'

print(indonesia)

# change the value of a key
indonesia['capital'] = 'Kutai Kartanegara'

print(indonesia)

print(len(indonesia.keys()))

# itterate through all the keys
for k in indonesia.keys():
    print(k)

for v in indonesia.values():
    print(v)

# the name is Republik Indonesia
# the population is ....
for k in indonesia.keys():
    print("The {0} is {1}".format(k, indonesia[k]))
    