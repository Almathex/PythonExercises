def isbn_check_number(first_12):
    first_12_without_dashes = first_12.replace("-", "")
    total = 0
    for index in range(12):
        if index % 2 == 0:
            total += int(first_12_without_dashes[index])
        else:
            total += (int(first_12_without_dashes[index])* 3)
    check_num = 10 - (total % 10)
    complete_number = first_12 + "-" +str(check_num)
    return complete_number

digits = input("Please enter the first 12 digits(with dashes): ")
print(isbn_check_number(digits))                