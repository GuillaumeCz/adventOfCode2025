
current = 50
solution = 0

with open('./day1_data.txt') as file:
    for line in file:
        li = line.rstrip()
        direction = li[0]
        nbr = int(li[1:])
        current = ((current - nbr) if direction ==
                   'L' else current + nbr) % 100

        if current == 0:
            solution += 1

print('-->', solution)
