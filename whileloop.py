counter = 0

while counter < 6:
    print(counter)
    counter += 1


ask = input("enter anything: ")

while len(ask) <= 0:
    ask = input("enter anything: ")

print(ask)
