# string checker
def is_string(value):
    return isinstance(value, str)

# string length checker
def is_string_length(value, length):
    return is_string(value) and len(value) == length

# numeric checker
def is_numeric(value):
    return isinstance(value, (int, float))

# special characters
def has_special_characters(value):
    if not is_string(value):
        return False
    special_characters = "!@#$%^&*()-+?_=,<>/"
    return any(char in special_characters for char in value)