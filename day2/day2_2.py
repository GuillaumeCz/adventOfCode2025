
solution = 0

invalids = []

# This is totaly not from me...
# It was stolen from the following repo:
# https://github.com/devalfie/adventofcode2025_python/blob/main/Day_2.py#L18
with open('./day2_data.txt') as file:
    for line in file:
        li = line.rstrip()
        ranges = []
        for range_str in line.rstrip().split(','):
            start, end = map(int, range_str.split('-'))
            ranges.append((start, end))
        for start, end in ranges:
            for candidate in range(start, end + 1):
                s = str(candidate)
                n = len(s)
                for seq_len in range(n // 2, 0, -1):
                    if n % seq_len == 0:
                        sequence = s[:seq_len]
                        repetitions = n // seq_len
                        if repetitions > 1 and sequence * repetitions == s:
                            invalids.append(candidate)

        solution = sum(set(invalids))

print('-->', solution)
