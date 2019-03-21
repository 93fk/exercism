def is_armstrong(number):
    str_num = str(number)
    len_num = len(str_num)
    sum = 0
    for n in str_num:
        sum += int(n)**len_num
    return sum == number
