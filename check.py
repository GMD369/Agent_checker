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