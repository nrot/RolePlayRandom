__author__ = 'nrot'

# -*- coding: utf-8 -*-

import random

import Source.classTree
import Source.ConstantFile as Constant
import Source.Function.f_table_to_list as Fttl


class ClassStarSistemRandom(object):
    def __init__(self):

        self.Planet = Source.classTree.classTree("Planet", None)
        self.Planet.parser(Fttl.table_to_list(Constant.PLANET_TABLE))

        self.Star = Source.classTree.classTree("Solar", None)
        self.Star.parser(Fttl.table_to_list(Constant.SOLAR_TABLE))

    def generate(self):

        amount_planet = random.randint(Constant.AMOUNT_PLANET_MIN, Constant.AMOUNT_PLANET_MAX)
        amount_star_in_system = random.randint(Constant.AMOUNT_STAR_IN_SYSTEM_MIN, Constant.AMOUNT_STAR_IN_SYSTEM_MAX)

        stars = []
        planets = []

        for i in range(0, amount_planet):
            planets.append(self.Planet.GetMask())
            planets.append(self.Planet.RandomItem())
        for i in range(0, amount_star_in_system):
            stars.append(self.Star.GetMask())
            stars.append(self.Star.RandomItem())
        return stars + planets
