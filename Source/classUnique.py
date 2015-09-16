__author__ = 'nrot'

# -*- coding: utf-8 -*-

import Source.classChance as classChance

class classUnique(object):
    def __init__(self, in_list):
        self.unique = []
        self.chance = []
        self.max = 0
        self.min = 100000  # Надо найти как называются константы

        i_i = 0

        for i in in_list:
            self.unique.append(i[0])
            self.chance.append(classChance.classChance(i[1]))
            if self.chance[i_i].maxChance > self.max:
                self.max = self.chance[i_i].maxChance
            if self.chance[i_i].minChance < self.min:
                self.min = self.chance[i_i].minChance
            i_i += 1

    def getRandomUnique(self):

        import random

        number = random.randint(self.min, self.max)

        flag = True
        i = 0

        while flag:
            if self.chance[i].minChance >= number and number <= self.chance[i].maxChance:
                return self.unique[i]
            i += 1