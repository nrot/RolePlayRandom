__author__ = 'nrot'

# -*- coding: utf-8 -*-

import Source.ConstantFile as Constant


def f_list_to_mask(list):

    if not list or not list[0]:
            return None

    mask = []
    flag_info = False
    flag_unique = False
    for i in list:
        if i == Constant.CHANCE:
            mask.append(Constant.CHANCE)
        elif i == Constant.INFO_START:
            flag_info = True
            mask.append(Constant.INFO_START)
        elif i == Constant.INFO_STOP:
            flag_info = False
            mask.append(Constant.INFO_STOP)
        elif i == Constant.UNIQUE_START:
            flag_unique = True
            mask.append(Constant.UNIQUE_START)
        elif i == Constant.UNIQUE_STOP:
            flag_unique = False
            mask.append(Constant.UNIQUE_STOP)
        elif i == Constant.COST:
            mask.append(Constant.COST)
        else:
            if flag_info:
                mask.append(Constant.INFO)
            elif flag_unique:
                mask.append(Constant.UNIQUE)
            else:
                mask.append(Constant.NAME_BRANCH)
    return mask
