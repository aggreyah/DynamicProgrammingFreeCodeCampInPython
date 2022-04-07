def grid_traveller(m, n):
    table = []

    for i in range(m + 1):
        row = []
        for j in range(n + 1):
            row.append(0)
        table.append(row)

    table[1][1] = 1

    for i in range(m + 1):
        for j in range(n + 1):
            current = table[i][j]
            if i + 1 <= m:
                table[i + 1][j] += current
            if j + 1 <= n:
                table[i][j + 1] += current

    return table[m][n]


if __name__ == "__main__":
    print(grid_traveller(1, 1))
    print(grid_traveller(2, 3))
    print(grid_traveller(3, 2))
    print(grid_traveller(3, 3))
    print(grid_traveller(58, 58))

