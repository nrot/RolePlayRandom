__author__ = 'nrot'

import random

import Source.ConstantFile as Constant
import Source.Function.f_Part_of_table as fpot
import Source.classCost as classCost
import Source.classUnique as classUnique


class classTree(object):
    def __init__(self, name, parentLink):
        self.name = name
        self.Parent = parentLink
        self.amount_branch = 0
        self.branchs = []
        self.info = []
        self.unique = None
        self.Cost = None
    def addBranch(self, branch, chance="one"):
        cache = [branch, chance]
        self.branchs.append(cache)
        self.amount_branch += 1

    def addInfo(self, info):
        self.info.append(info)

    def addUnique(self, unique):
        self.unique = classUnique.classUnique(unique)
    def parser(self, table):

        if not table or not table[0]:
            return

        mask = []
        flag_info = False
        flag_unique = False
        for i in table[0]:
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

        Vertical_mask = []
        v_i = 0
        for i in table:
            if i[0] != "" and i != table[0]:
                Vertical_mask.append(v_i)
                Iter = 0
                flag = True
                info_c = None
                while flag and Iter < len(mask) and Iter < len(i):
                    if mask[Iter] == Constant.NAME_BRANCH:
                        if Iter > 0:
                            flag = False
                            break
                        self.addBranch(classTree(i[Iter], self))
                        #self.addBranch(i[Iter], i[Iter+1])
                    elif mask[Iter] == Constant.INFO_START:
                        info_c = []
                        while mask[Iter] != Constant.INFO_STOP:
                            if mask[Iter] == Constant.COST:
                                self.Cost = classCost.classCost(i[Iter])
                            else:
                                info_c.append(i[Iter])
                            Iter += 1
                        self.branchs[self.amount_branch - 1][0].addInfo(info_c)
                    elif mask[Iter] == Constant.UNIQUE_START:
                        c_unique = []
                        while mask[Iter] != Constant.UNIQUE_STOP:
                            u = v_i
                            while table[u][Iter] != "":
                                if mask[Iter + 1] == Constant.CHANCE:
                                    c_unique.append([table[u][Iter], table[u][Iter + 1]])
                                elif mask[Iter] != Constant.CHANCE:
                                    c_unique.append(table[u][Iter])
                                u += 1
                            Iter += 1
                        self.branchs[self.amount_branch - 1][0].addUnique(c_unique)
                    Iter += 1
            v_i += 1
        Vertical_mask.append(len(table))

        flag = True
        Iter = 0
        for el_mask in mask:
            if el_mask == Constant.NAME_BRANCH:
                if flag:
                    flag = False
                else:
                    break
            Iter += 1

        v_i = 0
        for i in self.branchs:
            c_table = []

            c_table.append(fpot.f_Part_of_list(mask, Iter, len(mask)))
            z = Vertical_mask[v_i]
            while z < Vertical_mask[v_i + 1]:
                c_table.append(fpot.f_Part_of_table(table, Iter, len(mask), start_row=z, stop_row=z))
                z += 1
            v_i += 1
            i[0].parser(c_table)

    def RandomItem(self):
        c_list = ""
        c_list += self.name + " "

        if self.Cost:
            c_list += "Cost = " + str(self.Cost.getRandomCost()) + " "

        if self.branchs and self.branchs[0]:
            c_list += str(self.branchs[random.randint(0, self.amount_branch - 1)][0].RandomItem()) + " "

        if self.unique:
            c_list += str(self.unique.getRandomUnique()) + " "
        if self.info and self.info[0]:
            c_list += str(self.info)

        return c_list