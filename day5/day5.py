
def get_ranges():
    fresh_id_ranges = []
    ingredient_ids = []
    with open('./day5_sample.txt') as file:
        is_fresh_id_ranges = True
        for li in file:
            line = li.rstrip()
            if len(line.rstrip()) == 0:
                is_fresh_id_ranges = False
            else:
                if is_fresh_id_ranges:
                    fresh_id_ranges.append(line)
                else:
                    ingredient_ids.append(int(line))
    return fresh_id_ranges, ingredient_ids


def ranges_to_array(ran):
    ranges = []
    for r in ran:
        start, end = map(int, r.split('-'))
        ranges.append((start, end))
    return ranges


def part_1(fir, ii):
    ranges = ranges_to_array(fir)
    valid_ids = []

    for i_id in ii:
        for start, end in ranges:
            if i_id <= end and i_id >= start:
                valid_ids.append(i_id)

    valid_ids = set(valid_ids)
    return len(valid_ids)


def part_2(ranges):
    r = ranges_to_array(ranges)
    sr = sorted(r)
    merged = []
    for start, end in sr:
        if not merged or start > merged[-1][1] + 1:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    total = sum(end - start + 1 for start, end in r)
    return total


def main():
    solution = 0

    fresh_id_ranges, ingredient_ids = get_ranges()
    #  solution = part_1(fresh_id_ranges, ingredient_ids)
    solution = part_2(fresh_id_ranges)

    print('-->', solution)


if __name__ == "__main__":
    main()
