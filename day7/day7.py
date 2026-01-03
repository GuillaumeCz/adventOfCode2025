
def get_values():
    with open('./day7_data.txt') as file:
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


def main():
    solution = 0
    matrice = get_values()
    solution = part_1(matrice)
    print('-->', solution)


if __name__ == "__main__":
    main()
