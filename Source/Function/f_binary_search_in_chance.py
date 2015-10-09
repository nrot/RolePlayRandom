__author__ = 'nrot'

# -*- coding: utf-8 -*-


def f_binary_search_in_chance(list, search):
    l = 0
    r = len(list)
    m = (l + r) // 2
    if search >= list[m].maxChance:
        return m + f_binary_search_in_chance(list[m:r], search)
    elif search <= list[m].minChance:
        return m - f_binary_search_in_chance(list[l:m], search)
    elif (search >= list[m].minChance) and (search <= list[m].maxChance):
        return m
