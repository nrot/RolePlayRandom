__author__ = 'nrot'

# -*- coding: utf-8 -*-

import Source.Function.f_K_to_thousand as fktt

def f_Cost_to_list(in_str):
    first = True
    i_first = ""
    i_second = ""


    for i in in_str:
        if i == "-":
            first = False
            continue
        if first:
            i_first += i
        else:
            i_second += i

    i_first = fktt.f_K_to_thousand(i_first)
    i_second = fktt.f_K_to_thousand(i_second)

    if not i_second:
        return [int(i_first), int(i_first)]
    else:
        return [int(i_first), int(i_second)]
