# string checker
def is_string(value):
    return isinstance(value, str)

# string length checker
def is_string_length(value, length):
    return is_string(value) and len(value) == length

# numeric checker
def is_numeric(value):
    return isinstance(value, (int, float))

# positive number checker
def is_positive_number(value):
    return is_numeric(value) and value > 0

# string non-empty checker
def is_non_empty_string(value):
    return is_string(value) and len(value) > 0