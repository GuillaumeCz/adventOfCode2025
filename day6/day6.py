
def get_values():
    with open('./day6_data.txt') as file:
        matrice = []
        operations = []
        for li in file:
            if '*' in li:
                operations = li.split()
            else:
                matrice.append(li)

        return matrice, operations


def part_1(matrice, operations):
    solution = 0
    cols = []

    for i in range(len(matrice[0])):
        c = []
        for j in range(len(matrice)):
            c.append(matrice[j][i])
        cols.append(c)

    candidates = []

    for index, i in enumerate(cols):
        if operations[index] == '+':
            candidates.append(sum([int(z) for z in i]))
        else:
            acc = 1
            for j in i:
                acc = acc * int(j)
            candidates.append(acc)

    solution = sum(candidates)
    return solution


def part_2(matrice, operations):
    solution = 0

    cols = []
    for i in range(len(matrice[0])):
        c = []
        for j in range(len(matrice)):
            c.append(matrice[j][i])
        cols.append(c)

    nbr_char = int((len(cols) / len(operations)))

    cols = cols[:-1][::-1]

    accumulator = []
    groups_to_combine = []
    for index, col in enumerate(cols):
        if col.count(' ') != nbr_char + 1:
            c = int(''.join(col))
            accumulator.append(c)
        else:
            groups_to_combine.append(accumulator)
            accumulator = []

        if index == len(cols) - 1:
            groups_to_combine.append(accumulator)

    operations = operations[::-1]
    candidates = []
    for index, groups in enumerate(groups_to_combine):
        if operations[index] == '+':
            candidates.append(sum([int(z) for z in groups]))
        else:
            acc = 1
            for j in groups:
                acc = acc * j
            candidates.append(acc)

    solution = sum(candidates)

    return solution


def main():
    solution = 0
    matrice, operations = get_values()
    # solution = part_1(matrice, operations)
    solution = part_2(matrice, operations)
    print('-->', solution)


if __name__ == "__main__":
    main()
