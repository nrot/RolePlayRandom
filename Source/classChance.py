__author__ = 'nrot'

# -*- coding: utf-8 -*-


class classChance(object):
    def __init__(self, list):
        import Source.Function.f_Cost_to_list as fctl
        c_cost = fctl.f_Cost_to_list(list)

        self.minChance = c_cost[0]
        self.maxChance = c_cost[1]

    def getRandomChance(self):
        import random
        return random.randint(self.minChance, self.maxChance)