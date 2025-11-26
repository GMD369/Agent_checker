# string checker
def is_string(value):
    return isinstance(value, str)

# string length checker
def is_string_length(value, length):
    return is_string(value) and len(value) == length

# numeric checker
def is_numeric(value):
    return isinstance(value, (int, float))
