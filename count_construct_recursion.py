def count_construct(target_string, word_bank):
    if target_string == "":
        return 1

    count_ways = 0

    for word in word_bank:
        if target_string.startswith(word):
            suffix = target_string[len(word):]
            count_ways_remaining = count_construct(suffix, word_bank)
            count_ways += count_ways_remaining

    return count_ways


if __name__ == "__main__":
    print(count_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
    print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
    print(count_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]));
    print(count_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
    print(count_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))
