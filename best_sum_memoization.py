def best_sum(target_sum, int_list, a_dict):
    if target_sum in a_dict.keys():
        return a_dict[target_sum]
    if target_sum == 0:
        return list()
    if target_sum < 0:
        return None

    shortest_combination = None
    for item in int_list:
        remainder_combination = best_sum(target_sum - item, int_list, a_dict)
        if remainder_combination is not None:
            result_list = remainder_combination[:]
            result_list.append(item)
            if shortest_combination is None or len(remainder_combination) < len(shortest_combination):
                shortest_combination = result_list

    a_dict[target_sum] = shortest_combination
    return shortest_combination


if __name__ == "__main__":
    print(best_sum(7, [5, 3, 4, 7], dict()))
    print(best_sum(8, [2, 3, 5], dict()))
    print(best_sum(8, [1, 4, 5], dict()))
    print(best_sum(100, [1, 2, 5, 25], dict()))
