def grid_traveller(m, n, my_dict):
    m_n_string = str(m) + "," + str(n)
    m_n_string_reverse = reverse(m_n_string)

    if m_n_string in my_dict.keys():
        return my_dict[m_n_string]
    if m_n_string_reverse in my_dict.keys():
        return my_dict[m_n_string_reverse]

    if m == 0 or n == 0:
        return 0
    elif m == 1 and n == 1:
        return 1

    my_dict[m_n_string] = grid_traveller(m - 1, n, my_dict) + grid_traveller(m, n - 1, my_dict)
    return my_dict[m_n_string]


def reverse(s):
    string = ""
    for character in s:
        string = character + string
    return string


if __name__ == "__main__":
    print(grid_traveller(55, 55, dict()))
