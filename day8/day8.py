
def get_values():
    with open('./day7_sample.txt') as file:
        matrice = []
        for li in file:
            matrice.append(li.rstrip())

        return matrice


def part_1():
    solution = 0

    return solution


def part_2():
    solution = 0

    return solution


def main():
    matrice = get_values()
    solution = part_1()
    # solution = part_2()
    print('-->', solution)


if __name__ == "__main__":
    main()
