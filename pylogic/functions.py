# Globals #

global _
_ = None

# Case/Base Functions

def equal_or_empty(val1, val2):
    """Compares val1 and val2, returning True if they're equal or one of them is _"""

    if val1 == val2:
        return True
    elif val1 == _:
        return True
    elif val2 == _:
        return True
    else:
        return False

def compare_cases(case1, case2):
    """Compares case1 and case2, returning True if each cuple of values are equal_or_empty"""

    lista_bools = [(equal_or_empty(case1, case2)) for case1, case2 in zip(case1, case2)]
    return all(lista_bools)

def count_answers(tupla):
    """Counts the amount of _'s that exist in the tuple """

    lista, count = list(tupla), 0
    for l in lista:
            if l == _:
                count += 1
    return count

# Predicate Functions #

def flat(lista):
    """Flattens the elements of the list and returns them all in a single list"""

    new_list = []
    for lis in lista:
        if type(lis) == list:
            for l in lis:
                new_list.append(l)
        else:
            new_list.append(lis)
    return new_list

def eval_elems(lista):
    """Checks the boolean value of the list:
     - if one of them is False returns False
     - else it returns a list with the amount of True's """

    new_list = []
    for l in lista:
        if l is False:
            return False
        elif l is not True:
            new_list.append(l)
    return new_list

def format_rule(rule):
    """Receives a function an it transforms it to a Predicate """

    return lambda pred, tup: rule(tup)

def compare_tuple(tup1, tup2):
    """Compares two tuples arities and values """

    if len(tup1) != len(tup2):
        return False
    else:
        return tup1 == tup2

def check_tuple_elem(tup, lista):
    """Compares a tuple against a list of tuples """

    value = False
    for l in lista:
        value = compare_tuple(tup, l)
    return value

def filter_tuple_repeats(lista):
    """Filters repetitions of tuples in a list """

    new_list = []
    for l in lista:
        if not check_tuple_elem(l, new_list):
            new_list.append(l)
    return new_list
