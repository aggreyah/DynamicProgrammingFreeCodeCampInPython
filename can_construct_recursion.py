def can_construct(target_word, word_bank):
    if len(target_word) == 0:
        return True
    for word in word_bank:
        if target_word.startswith(word):
            suffix = target_word[len(word):]
            if can_construct(suffix, word_bank):
                return True
    return False


if __name__ == "__main__":
    print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
    print(can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]));
    print(can_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
    print(can_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))
