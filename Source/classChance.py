__author__ = 'nrot'

# -*- coding: utf-8 -*-


class ClassChance(object):
    def __init__(self, list):
        import Source.Function.f_cost_to_list as fctl

        c_cost = fctl.f_cost_to_list(list)

        self.minChance = c_cost[0]
        self.maxChance = c_cost[1]
        self.mean = float((self.maxChance + self.minChance) / 2)  # Среднее значение

    def get_random_chance(self):
        import random
        return random.randint(self.minChance, self.maxChance)
