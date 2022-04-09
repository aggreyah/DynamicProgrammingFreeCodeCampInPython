def all_construct(target_word, word_bank):
    table = []
    for i in range(len(target_word) + 1):
        table.append([])

    table[0].append([])

    for i in range(len(target_word) + 1):
        current_target = target_word[i:]
        if table[i]:
            for word in word_bank:
                if current_target.startswith(word) and i + len(word) <= len(target_word):
                    previous = []
                    for item in table[i]:
                        item_copy = item[:]
                        item_copy.append(word)
                        previous.append(item_copy)
                    table[i + len(word)].extend(previous)
    return table[len(target_word)]


if __name__ == "__main__":
    print(all_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
    print(all_construct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
    print(all_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]));
    print(all_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
    print(all_construct("aaaaaaaz", ["a", "aa", "aaa", "aaaa", "aaaaa"]))
