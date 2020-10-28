def near(string_1, string_2):
    list_1 = list(string_1)
    list_2 = list(string_2)
    for index in range(len(list_1)):
        remove_item = list_1[index]
        del list_1[index]
        if list_1 == list_2:
            return True
        list_1.insert(index, remove_item)
    return False

word1 = input("Please enter your first word: ")
word2 = input("Please enter your second word: ")

print(near(word1, word2))