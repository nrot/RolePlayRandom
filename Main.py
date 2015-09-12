__author__ = 'nrot'

# -*- coding: utf-8 -*-

import xlrd
import Source.FileClassPack
import Source.ConstantFile as Constant
import Source.LootRandom
import Source.f_Table_to_list as fttl

def main():

    Log = Source.FileClassPack.DoubleLog("./", 'log.txt')

    Input_string = ""

    LootRandom = Source.LootRandom.LootRandom()

    table = fttl.Table_to_list(Constant.GUNS_TABLE)

    Global_Run = True
    while (Global_Run):
        Input_string = input()
        if Input_string == u"Помощь":
            Log.write(aType='simple', text=Constant.BIG_HELP)
        elif Input_string == "LootRandom":
            LootRandom.Generate()


    return 0


if __name__ == "__main__":
    main()