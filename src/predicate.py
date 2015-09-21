from src.functions import format_rule, flat, eval_elems, _

class Predicate:

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
