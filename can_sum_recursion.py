def can_sum(target_sum, a_list):
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False
    for item in a_list:
        if can_sum(target_sum - item, a_list):
            return True
    return False


if __name__ == "__main__":
    print(can_sum(7, [2, 3]))
    print(can_sum(7, [5, 3, 4, 7]))
    print(can_sum(7, [2, 4]))
    print(can_sum(8, [2, 3, 5]))
    print(can_sum(300, [7, 14]))