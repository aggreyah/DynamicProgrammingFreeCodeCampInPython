def all_construct(target_word, word_bank):
    if target_word == "":
        empty_list_of_lists = list()
        empty_list_of_lists.append(list())
        return empty_list_of_lists

    result = list()
    for word in word_bank:
        if target_word.startswith(word):
            suffix = target_word[len(word):]
            suffix_construct = all_construct(suffix, word_bank)
            target_construct = suffix_construct[:]
            target_construct = list(map(lambda x: x.append(word), target_construct))
            result = list(map(lambda x: x, target_construct))
    return result


if __name__ == "__main__":
    print(all_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
    print(all_construct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
    print(all_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]));
    print(all_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
    # print(all_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))