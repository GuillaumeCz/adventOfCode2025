
solution = 0
candidates = []

with open('./day3_data.txt') as file:
    cpt = 0
    for line in file:

        bank = [int(s) for s in line.rstrip()]
        high = sorted(bank, reverse=True)[0]
        high_index = bank.index(high)

        right_section = bank[high_index + 1:]
        max_right = max(right_section) if len(right_section) > 0 else 0

        left_section = bank[:high_index]
        max_left = int(max(left_section)) if len(left_section) > 0 else 0

        right_s = int('{}{}'.format(int(high), max_right)
                      ) if max_right != 0 else 0
        left_s = int('{}{}'.format(max_left, int(high))
                     ) if max_left != 0 else 0

        candidates.append(max([right_s, left_s]))


solution = sum(candidates)

print(' -->', solution, )
