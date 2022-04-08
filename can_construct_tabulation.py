def can_construct(target_word, word_bank):
    table = []

    for i in range(len(target_word) + 1):
        table.append(False)

    table[0] = True

    for i in range(len(target_word) + 1):
        current_target = target_word[i:]
        if table[i]:
            for word in word_bank:
                if i + len(word) <= len(target_word) + 1 and current_target.startswith(word):
                    table[i + len(word)] = True

    return table[len(target_word)]


if __name__ == "__main__":
    print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
    print(can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
    print(can_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
    print(can_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))
