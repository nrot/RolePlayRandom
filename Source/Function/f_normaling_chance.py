__author__ = 'nrot'

# -*- coding: utf-8 -*-

def f_normaling_chance(in_str):

    first = True
    i_first = []
    i_second = []

    for i in in_str:
        if i == "-":
            first = False
            continue
        if first:
            i_first.append(i)
        else:
            i_second.append(i)

    if not i_second:
        return [int(i_first), int(i_first)]
    else:
        return [int(i_first), int(i_second)]
