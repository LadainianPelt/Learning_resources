def sum_str_lengths(L):
    """
    L is a non-empty list containing either: 
    * string elements or 
    * a non-empty sublist of string elements
    Returns the sum of the length of all strings in L and 
    lengths of strings in the sublists of L. If L contains an 
    element that is not a string or a list, or L's sublists 
    contain an element that is not a string, raise a ValueError.
    """
    total_length = 0
    for element in L:
        if isinstance(element, str):
            total_length += len(element)
        elif isinstance(element, list):
            for sub_element in element:
                if isinstance(sub_element, str):
                    total_length += len(sub_element)
                else:
                    raise ValueError("Sublists must contain only strings.")
        else:
            raise ValueError("List must contain only strings or sublists of strings.")
    return total_length