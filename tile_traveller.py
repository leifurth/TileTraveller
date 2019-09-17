x = 1
y = 1

def move_north(y):
    y += 1
    if y > 3:
        y = 3
    return y

def move_south(y):
    y -= 1
    if y < 1:
        y = 1
    return y

def move_east(x):
    x += 1
    if x > 3:
        x = 3
    return x

def move_west(x):
    x -= 1
    if x < 1:
        x = 1






if y == 1:
    print('You can travel: (N)orth.')
    direction = input('Direction: ')
    if direction == 'n' or direction == 'N':
        y = move_north(y)
    else:
        print(Not a valid direction!)

if


