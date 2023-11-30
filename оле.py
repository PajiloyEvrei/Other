def convert_integer(decimal, radix):
    if radix > 36:
        return "Основание системы счисления должно быть не больше 36-ти"
    number = ''
    while decimal > 0:
        decimal, remainder = divmod(decimal, radix)
        if remainder > 9:
            remainder = chr(ord('A') + remainder - 10)
        number = str(remainder) + number
    return number




        





