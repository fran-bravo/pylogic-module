from pylogic.case import Case
from pylogic.exceptions import ArityError, NoneBaseError


def case(knowledge_base):
    def wrap(func):
        def new_func(*args, **kwargs):
            if len(args) == knowledge_base.arity:
                new_case = Case(func.__name__, *args)

                knowledge_base.add_case(new_case)
                return func(*args, **kwargs)
            else:
                raise ArityError
        new_func.__name__ = func.__name__
        return new_func
    return wrap


def rule(predicate):
    def wrap(func):
        def new_func(*args, **kwargs):
            if predicate.base is not None:
                    predicate.add_rule(func)

                    return func(*args, **kwargs)
            else:
                raise NoneBaseError
        new_func.__name__ = func.__name__
        return new_func
    return wrap

