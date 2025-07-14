size = int(input('Enter the size of the pattern: '))

x = 1

while x <= size:
    y = 1
    while y <= size:
        print('*', end="")
        y += 1
    print()
    x += 1