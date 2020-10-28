def find_isbn(string_isbn):
    strip_isbn = string_isbn.replace('-','-')
    digit13 = 0
    x = 0
    leng = len(strip_isbn)
    while x < leng:
        num = int(strip_isbn[x])
        if (x % 2) == 0:
            digit13 += num
        else:
            digit13 += (num*3)
        x += 1
    digit = 10 - (digit13 % 10) 
    return digit