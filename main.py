field = ([[1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1]] * 10) + ([[0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1]] * 10)
while True:
    print("\n" + "\n".join(["".join('#' if j == 1 else ' ' for j in i) for i in field]))
    field = [[0 if (sum([field[(y + i - 1) % 20][(x + j - 1) % 20] for j in range(3) for i in range(3)]) - field[y][x]) <= 1 or (sum([field[(y + i - 1) % 20][(x + j - 1) % 20] for j in range(3) for i in range(3)]) - field[y][x]) >= 4 else 1 for x in range(len(field[y]))] for y in range(len(field))]
