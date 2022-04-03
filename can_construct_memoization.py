def can_construct(target_word, word_bank, a_dict):
    if target_word in a_dict.keys():
        return a_dict[target_word]
    if len(target_word) == 0:
        return True
    for word in word_bank:
        if target_word.startswith(word):
            suffix = target_word[len(word):]
            if can_construct(suffix, word_bank, a_dict):
                a_dict[target_word] = True
                return True
    a_dict[target_word] = False
    return False


if __name__ == "__main__":
    print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"], dict()))
    print(can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"], dict()));
    print(can_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"], dict()))
    print(can_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"], dict()))
