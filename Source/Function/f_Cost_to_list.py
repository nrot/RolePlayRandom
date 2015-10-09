__author__ = 'nrot'

# -*- coding: utf-8 -*-

import Source.Function.f_k_to_thousand as fktt


def f_cost_to_list(in_str):
    first = True
    i_first = ""
    i_second = ""
    new_str = ""

    if isinstance(in_str, float):
        new_str = str(int(in_str))
    elif in_str == "":
        new_str = "0"
    else:
        new_str = in_str

    for i in new_str:
        if i == "-":
            first = False
            continue
        if first:
            i_first += i
        else:
            i_second += i

    i_first = fktt.f_k_to_thousand(i_first)
    i_second = fktt.f_k_to_thousand(i_second)

    if not i_second:
        return [int(float(i_first)), int(float(i_first))]
    else:
        return [int(float(i_first)), int(float(i_second))]
