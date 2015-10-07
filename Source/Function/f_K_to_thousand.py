__author__ = 'nrot'


# -*- coding: utf-8 -*-

def f_k_to_thousand(in_str):
    i_number = ""
    for i in in_str:
        if i == "k" or i == "K" or i == u"к" or i == u"К":
            for z in range(0, 3):
                i_number += "0"
        else:
            i_number += i
    return i_number
