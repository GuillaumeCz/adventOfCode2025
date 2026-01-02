
solution = 0
candidates = []

#  Not that smart to solve this...
# Had to steal the solution from the following repo:
# https://github.com/devalfie/adventofcode2025_python/blob/main/Day_3.py
with open('./day3_data.txt') as file:
    for line in file:
        bank = [int(s) for s in line.rstrip()]
        L = len(bank)
        jolt_s = ''
        start = 0
        for i in range(12):
            v = -1
            end = L - 12 + 1 + i
            for j in range(start, end):
                c = bank[j]
                if c > v:
                    v = c
                    start = j + 1
            jolt_s += str(v)
        candidates.append(int(jolt_s))

solution = sum(candidates)

print(' -->', solution, )
