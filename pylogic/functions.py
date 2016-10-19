# Globals #

global _
_ = None

# Case/Base Functions


def equal_or_empty(tupla):
    """Compares a pair of values, returning True if they're equal or one of them is _

    :param tupla:
    """

    val1, val2 = tupla[0], tupla[1]
    if val1 == val2:
        return True
    elif val1 == _:
        return True
    elif val2 == _:
        return True
    else:
        return False


def all_satisfy(condition, lista):
    """ Checks if all the values from the list pass the condition

    :param lista:
    :param condition:
    """

    return all(map(condition, lista))


def compare_value_to_case(value, case):
    """ Compares a value against all the values in a case

        :param value:
        :param case:
    """

    for c in case:
        if(value == c and type(value) == type(c)) or (value == _):
            return True

    return False


def compare_cases(case1, case2):
    """Compares case1 and case2, returning True if each cuple of values are equal_or_empty

    :param case1:
    :param case2:
    """

    return all_satisfy(equal_or_empty, zip(case1, case2))


def _count_answers(tupla):
    """Counts the amount of _'s that exist in the tuple

    :param tupla:
    """

    lista, count = list(tupla), 0
    for l in lista:
            if l == _:
                count += 1
    return count


def count_answers(*variables):
    """Compatibility with *vars

        :param variables:
    """
    return _count_answers(variables)

# Predicate Functions #


def flat(lista):
    """Flattens the elements of the list and returns them all in a single list

    :param lista:
    """

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
     - else it returns a list with the amount of True's

     :param lista:
     """

    new_list = []
    for l in lista:
        if l is False:
            return False
        elif l is not True:
            new_list.append(l)
    return new_list


def format_rule(rule):
    """Receives a function an it transforms it to a Predicate

    :param rule:
    """

    return lambda pred, tup: rule(tup)


def compare_tuple(tup1, tup2):
    """Compares two tuples arities and values

    :param tup1:
    :param tup2:
    """

    if len(tup1) != len(tup2):
        return False
    else:
        return tup1 == tup2


def check_tuple_elem(tup, lista):
    """Compares a tuple against a list of tuples

    :param tup:
    :param lista:
    """

    value = False
    for l in lista:
        value = compare_tuple(tup, l)
    return value


def filter_tuple_repeats(lista):
    """Filters repetitions of tuples in a list

    :param lista:
    """

    new_list = []
    for l in lista:
        if not check_tuple_elem(l, new_list):
            new_list.append(l)
    return new_list
