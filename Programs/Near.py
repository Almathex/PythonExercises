def near_word(word, word2):
    word = word
    word2 = word2

    length = len(word)
    length2 = len(word2)
    if length2 > length:
        return False
    x = 0
    while x < length:
        wordtest2 = ''
        wordtest = list(word)
        del wordtest[x]
        wordtest2 = wordtest2.join(wordtest)
        print(wordtest2)

        if wordtest2 == word2:
            return True
        x +=1

    return False

if __name__ == '__main__':

    test = near_word("reset", "rest")
    print(test)           
