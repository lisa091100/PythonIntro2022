def turtle(coord, direction):
    arr = [i for i in range(4)]
    x, y = coord
    while True:
        c = yield x, y
        if c == 'f':
            if direction == 0:
                x += 1
            elif direction == 1:
                y += 1
            elif direction == 2:
                x -= 1
            else:
                y -= 1
        elif c == 'l':
            temp = arr[1:]+[arr[0]]
            direction = temp[direction]
        elif c == 'r':
            temp = [arr[-1]]+ arr[:-1]
            direction = temp[direction]
            
