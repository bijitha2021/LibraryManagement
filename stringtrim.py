def str_format(str, num):
    returnvalue = str

    length = len(str)
    if length < num:
        i = length
        while i <= num:
            str = str + " "
            i += 1
        returnvalue = str
    return returnvalue



