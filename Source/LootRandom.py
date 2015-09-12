__author__ = 'nrot'

# -*- coding: utf-8 -*-

import Source.ConstantFile as Constant
import random


class LootRandom(object):
    def __init__(self):



        random.seed()

    def Generate(self, size="medium"):

        Amount_Item = random.randint(Constant.AMOUNT_ITEM_MIN, Constant.AMOUNT_ITEM_MAX)
        Items = []
        Cans_Table = []
        i = 0
        if size == "small":
            Cans_Table.append(self.Item)
        elif size == "medium":
            Cans_Table.append(self.Item)
            Cans_Table.append(self.Guns)
        elif size == "big":
            Cans_Table.append(self.Item)
            Cans_Table.append(self.Guns)
            Cans_Table.append(self.Ship)

        while i < Amount_Item:
            choice_item = random.choice(Cans_Table)
            
            i += 1




