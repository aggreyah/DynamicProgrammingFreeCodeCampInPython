def how_sum(target_sum, ints_list):
    table = []
    for i in range(target_sum + 1):
        table.append(None)

    table[0] = []

    for i in range(target_sum + 1):
        if table[i] is not None:
            for num in ints_list:
                if i + num <= target_sum:
                    table[i + num] = table[i][:]
                    table[i + num].append(num)

    return table[target_sum]


if __name__ == "__main__":
    print(how_sum(7, [2, 3]))
    print(how_sum(7, [5, 3, 4, 7]))
    print(how_sum(7, [2, 4]))
    print(how_sum(8, [2, 3, 5]))
    print(how_sum(300, [7, 14]))
