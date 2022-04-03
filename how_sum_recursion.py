def how_sum(target_sum, ints_list):
    if target_sum == 0:
        return list()
    if target_sum < 0:
        return None

    for item in ints_list:
        result_list = how_sum(target_sum - item, ints_list)
        if result_list is not None:
            result_list.append(item)
            return result_list

    return None


if __name__ == "__main__":
    print(how_sum(7, [2, 3]))
    print(how_sum(7, [5, 3, 4, 7]))
    print(how_sum(7, [2, 4]))
    print(how_sum(8, [2, 3, 5]))
    print(how_sum(300, [7, 14]))
