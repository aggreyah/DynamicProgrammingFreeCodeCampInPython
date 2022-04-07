def can_sum(target_sum, ints_list):
    table = []
    for i in range(target_sum + 1):
        table.append(False)

    table[0] = True

    for i in range(target_sum + 1):
        if table[i]:
            for num in ints_list:
                if i + num <= target_sum:
                    table[i + num] = True

    return table[target_sum]


if __name__ == "__main__":
    print(can_sum(7, [2, 3]))
    print(can_sum(7, [5, 3, 4, 7]))
    print(can_sum(7, [2, 4]))
    print(can_sum(8, [2, 3, 5]))
    print(can_sum(300, [7, 14]))
