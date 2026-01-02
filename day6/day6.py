import re


def get_values():
    with open('./day6_data.txt') as file:
        matrice = []
        operations = []
        for li in file:
            p = re.sub(r'\ +', ' ', li.rstrip()).split(' ')
            if p[0].isdigit():
                matrice.append(p)
            else:
                operations = p

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


def main():
    solution = 0
    matrice, operations = get_values()
    solution = part_1(matrice, operations)
    print('-->', solution)


if __name__ == "__main__":
    main()
