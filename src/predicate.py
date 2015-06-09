def reduce_lvl(lista):
    new_list = []
    for l in lista:
        new_list = l
    return new_list

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
    new_rule = lambda pred, tup: rule(tup)
    return new_rule


class Predicate():

    def __init__(self):
        self.rules = []
        self.base_rule = None
        self.bases = []
        self.main_rule()
        self.results = []

    def add_base(self, base):
        self.bases.append(base)

    def add_rule(self, rule):
        self.rules.append(format_rule(rule))

    def main_rule(self):
        self.base_rule = lambda pred, tup: flat([base.tally(tup) for base in pred.bases])

    def tally_main(self, params):
        self.results = self.base_rule(self, params)

    def tally_rules(self, params):
        aux = []
        for result in self.results:
            if self.rules != []:
                if True in [rule(self, result) for rule in self.rules]:
                    aux.append(result)
            else:
                aux = self.results
        self.results = aux

    def tally(self, params):
        self.tally_main(params)
        self.tally_rules(params)

        return eval_elems(self.results)
