
def get_ranges():
    fresh_id_ranges = []
    ingredient_ids = []
    with open('./day5_data.txt') as file:
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


def part_1(fir, ii):
    ranges = []
    for r in fir:
        sp = r.split('-')
        min = int(sp[0])
        max = int(sp[1])
        ranges.append([min, max])
    valid_ids = []

    for i_id in ii:
        for r in ranges:
            if i_id <= r[1] and i_id >= r[0]:
                valid_ids.append(i_id)

    valid_ids = set(valid_ids)
    return len(valid_ids)


def main():
    solution = 0

    fresh_id_ranges, ingredient_ids = get_ranges()
    solution = part_1(fresh_id_ranges, ingredient_ids)

    print('-->', solution)


if __name__ == "__main__":
    main()
