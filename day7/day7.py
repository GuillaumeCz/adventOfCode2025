
# I did not succeed into this part 2 of the seventh day of advent of code.
def get_values():
    with open('./day7_sample.txt') as file:
        matrice = []
        for li in file:
            matrice.append(li.rstrip())

        return matrice


def part_1(matrice):
    solution = 0

    ma = matrice[::-1]

    for line_index, line in enumerate(ma):
        for char_index, char in enumerate(line):
            if char == '^':
                splits = False
                cpt = line_index + 1
                go = True
                while go:
                    if ma[cpt][char_index - 1] == '^' or ma[cpt][char_index + 1] == '^':
                        splits = True
                        go = False

                    elif ma[cpt][char_index] == '^':
                        go = False
                        if not splits:
                            solution += 1

                    if cpt >= len(ma) or ma[cpt][char_index] == 'S':
                        go = False
                    cpt += 1

    c = 0
    for i in matrice:
        c += i.count('^')
    solution = c - solution

    return solution


def get_route(matrice, line, col, total, known):
    if matrice[line][col] == '.' or matrice[line][col] == 'S':
        known.append((line, col))
    elif matrice[line][col] == '^':
        acc = 0
        # Makes everything crash because to heavy...
        #  Need optimisation... !
        # if (line, col + 1) not in known and matrice[line][col + 1] == '.':
        acc += get_route(matrice, line, col + 1, total, known)

        # if (line, col - 1) not in known and matrice[line][col - 1] == '.':
        acc += get_route(matrice, line, col - 1, total, known)

        total += acc
        return total

    line += 1
    if line < len(matrice):
        return get_route(matrice, line, col, total, known)
    else:
        total += 1
        print('+1', line, col + 1)
        return total


def part_2(matrice):
    solution = 0

    line = 0
    col = matrice[0].index('S')

    solution = get_route(matrice, line, col, 0, [])

    return solution


def main():
    matrice = get_values()
    # solution = part_1(matrice)
    solution = part_2(matrice)
    print('-->', solution)


if __name__ == "__main__":
    main()
