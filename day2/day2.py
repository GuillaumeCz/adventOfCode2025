
solution = 0

with open('./day2_data.txt') as file:
    for line in file:
        li = line.rstrip()
        ranges = li.split(',')
        for r in ranges:
            s = r.split('-')
            for i in range(int(s[0]), int(s[1]) + 1):
                s = str(i)
                if len(s) % 2 == 0:
                    half = len(s) // 2
                    if s[:half] == s[half:]:
                        solution += i


print('-->', solution)
