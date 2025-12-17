# string checker
def is_string(value):
    return isinstance(value, str)

# integer checker
def is_integer(value):
    return isinstance(value, int)
# float checker
def is_float(value):
    return isinstance(value, float)

# list checker
def is_list(value):
    return isinstance(value, list)

# dictionary checker
def is_dictionary(value):
    return isinstance(value, dict)

# boolean checker
def is_boolean(value):
    return isinstance(value, bool)

# tuple checker
def is_tuple(value):
    return isinstance(value, tuple)

# set checker
def is_set(value):
    return isinstance(value, set)

# none checker
def is_none(value):
    return value is None