__author__ = 'nrot'

# -*- coding: utf-8 -*-

import random

import Source.ConstantFile as Constant
import Source.classTree
import Source.Function.f_Table_to_list as fttl


class LootRandom(object):
    def __init__(self):

        self.Guns = Source.classTree.classTree("Gun", None)
        self.Guns.parser(fttl.Table_to_list(Constant.GUNS_TABLE))

        """self.Item = Source.classTree.classTree("Item", None)
        self.Item.parser(fttl.Table_to_list(Constant.ITEM_TABLE))"""


        #random.seed()

    def Generate(self, size="medium"):

        Amount_Item = random.randint(Constant.AMOUNT_ITEM_MIN, Constant.AMOUNT_ITEM_MAX)
        Items = []
        Cans_Table = []
        i = 0
        item = []
        if size == "small":
            #Cans_Table.append(self.Item)
            0
        elif size == "medium":
           #Cans_Table.append(self.Item)
            Cans_Table.append(self.Guns)
        elif size == "big":
            #Cans_Table.append(self.Item)
            Cans_Table.append(self.Guns)
            #Cans_Table.append(self.Ship)

        while i < Amount_Item:
            choice_item = random.choice(Cans_Table)
            item.append(choice_item.RandomItem())
            i += 1
        return item



