peaksint = [0, 8, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]


def route(list_1):
    ideal = []
    for index in range(len(list_1)):
        if index == 0:
            ideal.append(list_1[index])
        elif ideal[index - 1] < list_1[index]:
            ideal.append(list_1[index])
        elif ideal[index - 1] > list_1[index]:
            ideal.append(ideal[index - 1])
            continue
    return ideal


def noreps(list_1):
    ideal = []
    for number in list_1:
        if list_1.index(number) == (len(list_1) - 1):
            ideal.append(number)
            break
        elif len(ideal) == 0:
            ideal.append(number)
        elif number in ideal:
            continue
        else:
            ideal.append(number)
    return ideal


answer = route(peaksint)
answer2 = noreps(answer)
print(answer2)