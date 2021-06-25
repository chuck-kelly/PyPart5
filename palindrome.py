def is_palindrome(value: str) -> bool:
    """
    This function determines if a word or phrase is a palindrome

    :param value: A string
    :return: A boolean
    """
    
    value_arr = list(value)
    removes = value_arr.remove(' ')
    while True:
        if ' ' in value_arr:
            removes = value_arr.remove(' ')
        else:
            break
    new_str = ''
    for letter in value_arr:
        new_str = new_str + letter

    new_str = new_str.lower()
    backwards = new_str[::-1]
    print(new_str)
    print(backwards)
    if new_str == backwards:
        return True
    else:
        return False


