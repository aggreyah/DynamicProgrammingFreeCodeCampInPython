def best_sum(target_sum, ints_list):
    table = []

    for i in range(target_sum + 1):
        table.append(None)

    table[0] = []

    for i in range(target_sum + 1):
        if table[i] is not None:
            for num in ints_list:
                if i + num <= target_sum:
                    current = table[i][:]
                    current.append(num)
                    if table[i + num] is None or len(table[i + num]) > len(current):
                        table[i + num] = current[:]

    return table[target_sum]


if __name__ == "__main__":
    print(best_sum(7, [5, 3, 4, 7]))
    print(best_sum(8, [2, 3, 5]))
    print(best_sum(8, [1, 4, 5]))
    print(best_sum(200, [25, 2, 5, 1]))
