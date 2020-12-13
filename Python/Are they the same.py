def comp(array1, array2, power=2):
    if array1 is None or array2 is None:
        return False
    if len(array1) == 0 and len(array2) == 0:
        return True
    for item in array1:
        item = int(item)
        check = item ** power
        if check in array2:
            array2.remove(check)
            continue
        else:
            return False
    if len(array2) == 0:
        return True
    else:
        return False
