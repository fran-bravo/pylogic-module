from pylogic.functions import format_rule, flat, eval_elems, _


class Predicate:
    """Advanced logical object that establishes rules associated to cases and other kind of rules, contains:
    - A list of rules that are applied to the queries associated to it. One of them is a KnowledgeBase query
    - A knowledgeBase, that is used in the queries
    - A list of results, that is used for handling the responses
    """

# Magic Methods #

    def __init__(self, selector="default", base=None):
        self.rules = []
        self.base_rule = None
        self.base = base
        self._main_rule(selector)
        self._results = []

    def __str__(self):
        return "Rules: " + str(self.rules) + " Base: " + str(self.base) + " Results: " + str(self._results)

# Auxiliary Methods #

    def _main_rule(self, selector):
        self.base_rule = lambda pred, tup: self.base.tally(selector, *tup)

    def _tally_main(self, params):
        self._results = self.base_rule(self, params)

    def _tally_rules(self, params):
        aux = []
        for result in self._results:
            if self.rules != []:
                if all([rule(self, result) for rule in self.rules]):
                    aux.append(result)
            else:
                aux = self._results
        self._results = aux

# Public Interface #

    def add_base(self, base):
        self.base = base

    def add_rule(self, rule):
        self.rules.append(format_rule(rule))

    def tally(self, *params):
        pars = tuple(params)
        self._tally_main(pars)
        self._tally_rules(pars)

        return eval_elems(self._results)
