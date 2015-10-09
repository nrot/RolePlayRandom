__author__ = 'nrot'

# -*- coding: utf-8 -*-

import random

import Source.ConstantFile as Constant
import Source.ClassTree
import Source.Function.f_table_to_list as Fttl


class LootRandom(object):
    def __init__(self):

        self.Guns = Source.ClassTree.ClassTree("Gun", None)
        self.Guns.parser(Fttl.table_to_list(Constant.GUNS_TABLE))

        """self.Item = Source.classTree.classTree("Item", None)
        self.Item.parser(Fttl.Table_to_list(Constant.ITEM_TABLE))"""

        # random.seed()

    def generate(self, size="medium"):

        amount_item = random.randint(Constant.AMOUNT_ITEM_MIN, Constant.AMOUNT_ITEM_MAX)
        cans_table = []
        item = []
        if size == "small":
            # cans_table.append(self.Item)
            0
        elif size == "medium":
            # cans_table.append(self.Item)
            cans_table.append(self.Guns)
        elif size == "big":
            # cans_table.append(self.Item)
            cans_table.append(self.Guns)
            # cans_table.append(self.Ship)
        prev = None
        for i in range(0, amount_item):
            choice_item = random.choice(cans_table)
            if i != 0 and prev != choice_item:
                item.append(choice_item.get_mask())
            elif i == 0:
                item.append(choice_item.get_mask())
            item.append(choice_item.random_item())
            prev = choice_item
        return item
