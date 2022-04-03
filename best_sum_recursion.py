def best_sum(target_sum, int_list):
    if target_sum == 0:
        return list()
    if target_sum < 0:
        return None

    shortest_combination = None
    for item in int_list:
        remainder_combination = best_sum(target_sum - item, int_list)
        if remainder_combination is not None:
            result_list = remainder_combination[:]
            result_list.append(item)
            if shortest_combination is None or len(remainder_combination) < len(shortest_combination):
                shortest_combination = result_list

    return shortest_combination


if __name__ == "__main__":
    print(best_sum(7, [5, 3, 4, 7]))
    print(best_sum(8, [2, 3, 5]))
    print(best_sum(8, [1, 4, 5]))
    print(best_sum(50, [1, 2, 5, 25]))
