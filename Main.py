__author__ = 'nrot'

# -*- coding: utf-8 -*-

import xlrd
import Source.FileClassPack
import Source.ConstantFile as Constant
import Source.LootRandom
import Source.StarSystemRandom


def main():
    Log = Source.FileClassPack.DoubleLog("./", 'log.txt')

    input_string = ""

    loot_random = Source.LootRandom.LootRandom()
    star_system_random = Source.StarSystemRandom.ClassStarSistemRandom()

    global_run = True
    while global_run:
        input_string = input()
        if input_string == u"Помощь" or input_string == "Help" or input_string == "/h":
            Log.write(atype='simple', text=Constant.BIG_HELP)
        elif input_string == "LootRandom":
            l = loot_random.generate()
            for i in l:
                print(i)
                # print(str(LootRandom.Generate()))
        elif input_string == "RandomStarSystem":
            l = star_system_random.generate()
            for i in l:
                print(i)

    return 0


if __name__ == "__main__":
    main()
