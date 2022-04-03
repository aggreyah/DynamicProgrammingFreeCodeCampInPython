def count_construct(target_string, word_bank, a_dict):
    if target_string in a_dict.keys():
        return a_dict[target_string]
    if target_string == "":
        return 1

    count_ways = 0

    for word in word_bank:
        if target_string.startswith(word):
            suffix = target_string[len(word):]
            count_ways_remaining = count_construct(suffix, word_bank, a_dict)
            count_ways += count_ways_remaining

    a_dict[target_string] = count_ways
    return count_ways


if __name__ == "__main__":
    print(count_construct("purple", ["purp", "p", "ur", "le", "purpl"], dict()))
    print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"], dict()))
    print(count_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"], dict()));
    print(count_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"], dict()))
    print(count_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"],
                          dict()))
