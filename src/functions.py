# Globals #

global _
_ = None

# Case/Base Functions

def equal_or_empty(val1, val2):
    if val1 == val2:
        return True
    elif val1 == _:
        return True
    elif val2 == _:
        return True
    else:
        return False

def compare_cases(case1, case2):
    lista_bools = [(equal_or_empty(case1, case2)) for case1, case2 in zip(case1, case2)]
    return all(lista_bools)

def count_answers(tupla):
    lista, count = list(tupla), 0
    for l in lista:
            if l == _:
                count += 1
    return count

# Predicate Functions #

def reduce_lvl(lista):
    for l in lista:
        return l


def flat(lista):
    new_list = []
    for lis in lista:
        if type(lis) == list:
            for l in lis:
                new_list.append(l)
        else:
            new_list.append(lis)
    return new_list

def eval_elems(lista):
    new_list = []
    for l in lista:
        if l is False:
            return False
        elif l is not True:
            new_list.append(l)
    return new_list

def format_rule(rule):
    return lambda pred, tup: rule(tup)

def compare_tuple(tup1, tup2):
    if len(tup1) != len(tup2):
        return False
    else:
        for i in range(len(tup1)):
            if tup1[i] != tup2[i]:
                return False

    return True

def check_tuple_elem(tup, lista):
    value = False
    for l in lista:
        value = compare_tuple(tup, l)
    return value

def filter_tuple_repeats(lista):
    new_list = []
    for l in lista:
        if not check_tuple_elem(l, new_list):
            new_list.append(l)
    return new_list
