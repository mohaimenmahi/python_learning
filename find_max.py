def find_max_val(list):
    sz = len(list)

    list.sort()

    return list[sz - 1]