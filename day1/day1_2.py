current = 50
solution = 0

with open('./day2_data.txt') as file:
    for line in file:
        li = line.rstrip()
        direction = li[0]
        nbr = int(li[1:])

        if direction == 'L':
            start = current
            end = current - nbr
            for i in range(start, end, -1):
                if i % 100 == 0:
                    solution += 1
        else:
            start = current
            end = current + nbr
            for i in range(start, end, 1):
                if i % 100 == 0:
                    solution += 1

        current = (current - nbr if direction == 'L' else current + nbr) % 100

print('-->', solution)
