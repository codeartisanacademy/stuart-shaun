fruits = ['apple', 'orange', 'durian']

print(len(fruits))

# get one item from the list
print(fruits[1])

# add a new item to the end of the list
fruits.append('lychee')

print(len(fruits))

print(fruits)

fruits.insert(1, 'strawberry')

fruits.sort(reverse=True)

print(fruits)

print(fruits.count('apple'))

print(fruits.index('orange'))

# for loop to iterate through the list 
for f in fruits:
    print('the fruit is ' + f.upper())