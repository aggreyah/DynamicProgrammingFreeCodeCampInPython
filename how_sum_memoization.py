def how_sum(target_sum, ints_list, a_dict):
    if target_sum in a_dict.keys():
        return a_dict[target_sum]
    if target_sum == 0:
        return list()
    if target_sum < 0:
        return None

    for item in ints_list:
        result_list = how_sum(target_sum - item, ints_list, a_dict)
        if result_list is not None:
            result_list.append(item)
            a_dict[target_sum] = result_list
            return a_dict[target_sum]

    a_dict[target_sum] = None
    return None


if __name__ == "__main__":
    print(how_sum(7, [2, 3], dict()))
    print(how_sum(7, [5, 3, 4, 7], dict()))
    print(how_sum(7, [2, 4], dict()))
    print(how_sum(8, [2, 3, 5], dict()))
    print(how_sum(5368, [7, 14], dict()))
