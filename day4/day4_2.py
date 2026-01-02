solution = 0


def has_fewer_rools(matrice, col, line):
    col_range = [-1, 0, 1]
    line_range = [-1, 0, 1]
    if col == 0:
        col_range = [0, 1]
    elif col == len(matrice) - 1:
        col_range = [-1, 0]

    if line == 0:
        line_range = [0, 1]
    elif line == len(matrice[col]) - 1:
        line_range = [-1, 0]

    nbr = 0

    for col_index in col_range:
        for line_index in line_range:
            if not (line_index == 0 and col_index == 0):
                if matrice[col + col_index][line + line_index] == '@':
                    nbr += 1
    return nbr < 4


with open('./day4_data.txt') as file:
    matrice = []
    row_length = 0
    col_length = 0
    for i, l in enumerate(file):
        matrice.append([str(s) for s in l.rstrip()])
        row_length = len(l)

    col_length = len(matrice)

    to_continue = True

    while to_continue:
        candidates = 0
        coords_to_erase = []
        for col in range(col_length):
            for line in range(row_length - 1):
                if matrice[col][line] == '@' and has_fewer_rools(matrice, col, line):
                    coords_to_erase.append([col, line])
                    candidates += 1
        if candidates == 0:
            to_continue = False

        solution += candidates

        for c in coords_to_erase:
            matrice[c[0]][c[1]] = '.'

print('-->', solution)
