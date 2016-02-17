from src.case import Case
from src.exceptions import ArityError

def case(knowledge_base):
    def wrap(func):
        def new_func(*args,**kwargs):
            if(len(args) == knowledge_base.arity):
                new_case = Case(func.__name__, *args)

                knowledge_base.add_case(new_case)
                return func(*args,**kwargs)
            else:
                raise ArityError
        new_func.__name__ = func.__name__
        return new_func
    return wrap