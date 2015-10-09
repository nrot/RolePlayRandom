__author__ = 'nrot'

# -*- coding: utf-8 -*-

import random

import Source.ClassTree
import Source.ConstantFile as Constant
import Source.Function.f_table_to_list as Fttl


class ClassStarSistemRandom(object):
    def __init__(self):
        try:
            self.Planet = Source.ClassTree.ClassTree("Planet", None)
        except:
            None
        try:
            self.Planet.parser(Fttl.table_to_list(Constant.PLANET_TABLE))
        except:
            None
        try:
            self.Star = Source.ClassTree.ClassTree("Solar", None)
        except:
            None
        try:
            self.Star.parser(Fttl.table_to_list(Constant.SOLAR_TABLE))
        except:
            None
    # TODO: Добавить генерацию картинки звездный системы

    def generate(self):

        amount_planet = random.randint(Constant.AMOUNT_PLANET_MIN, Constant.AMOUNT_PLANET_MAX)
        amount_star_in_system = random.randint(Constant.AMOUNT_STAR_IN_SYSTEM_MIN, Constant.AMOUNT_STAR_IN_SYSTEM_MAX)

        stars = []
        planets = []

        for i in range(0, amount_planet):
            planets.append(self.Planet.get_mask())
            planets.append(self.Planet.random_item())
        for i in range(0, amount_star_in_system):
            stars.append(self.Star.get_mask())
            stars.append(self.Star.random_item())
        return stars + planets
