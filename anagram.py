def is_anagram(first_string: str, second_string: str) -> bool:
    """
    Given two strings, this functions determines if they are an anagram of one another.
    """

    first_arr = list(first_string)
    second_arr = list(second_string)
    
    #remove spaces
    while True:
        if ' ' in first_arr:
            removes = first_arr.remove(' ')
        else:
            break

    
    while True:
        if ' ' in second_arr:
            removes = second_arr.remove(' ')
        else:
            break
    #make letters all lower case and sort
    for letter in first_arr:
        letter.lower()

    for letter in second_arr:
        letter.lower()

    first_arr.sort()
    second_arr.sort() 

    '''
    new_str_first = ''
    for letter in first_arr:
        new_str_first = new_str_first + letter

    new_str_second = ''
    for letter in second_arr:
        new_str_second = new_str_second + letter

    '''
    if first_arr == second_arr:
        return True
    else:
        return False
    

