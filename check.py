# check zero division
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

# check list index out of range
def safe_get(lst, index):
    try:
        return lst[index]
    except IndexError:
        return None
    
# check key error in dictionary
def safe_get_dict(dct, key):
    try:
        return dct[key]
    except KeyError:
        return None

# def add
def add(a,b):
    return a+b