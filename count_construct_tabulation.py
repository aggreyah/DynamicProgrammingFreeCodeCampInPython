def count_construct(target_word, word_bank):
    table = []
    for i in range(len(target_word) + 1):
        table.append(0)

    table[0] = 1

    for i in range(len(target_word) + 1):
        current_target = target_word[i:]
        if table[i]:
            for word in word_bank:
                if current_target.startswith(word) and i + len(word) <= len(target_word):
                    table[i + len(word)] += table[i]

    return table[len(target_word)]


if __name__ == "__main__":
    print(count_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
    print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd", "d", "ef"]))
    print(count_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]));
    print(count_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
    print(count_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))
