def best_conjug(word_1):
    word_2 = word_1.lower()
    words = []
    with open("./Programs/wordlist.txt", "r") as file:
        lines = file.readlines()
    for line in lines:
        n1 = line.replace('\n', '') 
        if n1 in word_2 and len(n1) >= 2 and len(n1) < len(word_2):
            words.append(n1)
    return words 
def sorting(words): 
    lst2 = sorted(words, key=(len)) 
    lst3 = lst2[::-1]
    return lst3

print(sorting(best_conjug("Superman")))