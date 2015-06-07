__author__ = 'francisco'

class Predicate():

    def __init__(self):
        self.rules = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def tally(self, vars):
        return map(lambda x: x.tally(vars), self.rules)
