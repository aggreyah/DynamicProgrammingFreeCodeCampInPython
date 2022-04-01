def can_sum(target_sum, a_list, a_dict):
    if target_sum in a_dict.keys():
        return a_dict[target_sum]
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False
    for item in a_list:
        if can_sum(target_sum - item, a_list, a_dict):
            a_dict[target_sum] = True
            return True
    a_dict[target_sum] = False
    return False


if __name__ == "__main__":
    print(can_sum(7, [2, 3], dict()))
    print(can_sum(7, [5, 3, 4, 7], dict()))
    print(can_sum(7, [2, 4], dict()))
    print(can_sum(8, [2, 3, 5], dict()))
    print(can_sum(3500, [7, 14], dict()))
