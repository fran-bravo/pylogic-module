from pylogic.functions import format_rule, flat, eval_elems, _

class Predicate:
    """Advanced logical object that establishes rules associated to cases and other kind of rules, contains:
    - A list of rules that are applied to the queries associated to it. One of them is a KnowledgeBase query
    - A list of knowledgeBases, that are used in the queries
    - A list of results, that is used for handling the responses
    """

    def __init__(self, selector="default"):
        self.rules = []
        self.base_rule = None
        self.bases = []
        self.main_rule(selector)
        self._results = []

    def __str__(self):
        bases = []
        for b in self.bases:
            bases.append(str(b))
        return "Rules: " + str(self.rules) + " Bases: " + str(bases) + " Results: " + str(self._results)

    def add_base(self, base):
        self.bases.append(base)

    def add_rule(self, rule):
        self.rules.append(format_rule(rule))

    def main_rule(self, selector):
        self.base_rule = lambda pred, tup: flat([base.tally(selector, *tup) for base in pred.bases])

    def tally_main(self, params):
        self._results = self.base_rule(self, params)

    def tally_rules(self, params):
        aux = []
        for result in self._results:
            if self.rules != []:
                if True in [rule(self, result) for rule in self.rules]:
                    aux.append(result)
            else:
                aux = self._results
        self._results = aux

    def tally(self, *params):
        pars = tuple(params)
        self.tally_main(pars)
        self.tally_rules(pars)

        return eval_elems(self._results)
