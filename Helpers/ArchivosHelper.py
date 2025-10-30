def fix_info(l):
    list = l.split(";")
    list[-1] = list[-1].strip("\n")
    return list