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
        matrice.append(l.rstrip())
        row_length = len(l)

    col_length = len(matrice)

    for col in range(col_length):
        for line in range(row_length - 1):
            if matrice[col][line] == '@':
                if has_fewer_rools(matrice, col, line):
                    solution += 1

print('-->', solution)
