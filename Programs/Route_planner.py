numblist = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
for i in numblist:
    try:
        if numblist[i] > numblist[i + 1]:
            continue
        else:
            print(i)
    except:
        pass
 #NOT FINISHED DOESNT ONLY INCREASE YET