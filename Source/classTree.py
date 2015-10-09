__author__ = 'nrot'

import random

import Source.ConstantFile as Constant
import Source.Function.f_part_of_table as fpot
import Source.classCost as classCost
import Source.ClassUnique as classUnique
import Source.Function.f_list_to_mask as fltm
import Source.ClassChance as classChance
import Source.Function.f_sorted_chance as fsc


class ClassTree(object):
    def __init__(self, name, parent_link):
        self.name = name
        self.Parent = parent_link
        self.amount_branch = 0
        self.branchs = []
        self.chance_branch = []
        self.info = []
        self.unique = None
        self.Cost = None
        self.Mask = None
        self.list_to_mask = fltm.f_list_to_mask

    def add_branch(self, branch, chance="one"):

        if chance == "one":
            cache = [branch, chance]
            self.branchs.append(cache)
            cache = (1 / len(self.branchs)) * 100
            for i in range(1, len(self.branchs) + 1):
                self.branchs[i - 1][1] = classChance.ClassChance(str((i - 1) * cache) + " - " + str(i * cache))
        else:
            cache = [branch, classChance.ClassChance(chance)]
            self.branchs.append(cache)
        self.amount_branch += 1

    def add_info(self, info):
        self.info.append(info)

    def add_unique(self, unique):
        self.unique = classUnique.ClassUnique(unique)

    def parser(self, table):

        if table and table[0]:
            self.Mask = self.list_to_mask(table[0])
        else:
            return

        vertical_mask = []
        v_i = 0
        for i in table:
            if i[0] != "" and i != table[0]:
                vertical_mask.append(v_i)
                iteration = 0
                flag = True
                while flag and iteration < len(self.Mask) and iteration < len(i):
                    if self.Mask[iteration] == Constant.NAME_BRANCH:
                        if iteration > 0:
                            flag = False
                            break
                        if self.Mask[iteration + 1] == Constant.CHANCE:
                            self.add_branch(ClassTree(i[iteration], self), chance=i[iteration + 1])
                        else:
                            self.add_branch(ClassTree(i[iteration], self))
                        # self.addBranch(i[iteration], i[iteration+1])
                    elif self.Mask[iteration] == Constant.INFO_START:
                        info_c = []
                        while self.Mask[iteration] != Constant.INFO_STOP:
                            if self.Mask[iteration] == Constant.COST:
                                self.Cost = classCost.classCost(i[iteration])
                            else:
                                info_c.append(i[iteration])
                            iteration += 1
                        self.branchs[self.amount_branch - 1][0].add_info(info_c)
                    elif self.Mask[iteration] == Constant.UNIQUE_START:
                        c_unique = []
                        while self.Mask[iteration] != Constant.UNIQUE_STOP:
                            u = v_i
                            while table[u][iteration] != "":
                                if self.Mask[iteration + 1] == Constant.CHANCE:
                                    c_unique.append([table[u][iteration], table[u][iteration + 1]])
                                elif self.Mask[iteration] != Constant.CHANCE:
                                    c_unique.append(table[u][iteration])
                                u += 1
                            iteration += 1
                        self.branchs[self.amount_branch - 1][0].add_unique(c_unique)
                    iteration += 1
            v_i += 1
        vertical_mask.append(len(table))

        flag = True
        iteration = 0
        for el_mask in self.Mask:
            if el_mask == Constant.NAME_BRANCH:
                if flag:
                    flag = False
                else:
                    break
            iteration += 1

        v_i = 0
        for i in self.branchs:
            c_table = [fpot.f_part_of_list(self.Mask, iteration, len(self.Mask))]
            for z in range(vertical_mask[v_i], vertical_mask[v_i + 1]):
                c_table.append(fpot.f_part_of_table(table, iteration, len(self.Mask), start_row=z, stop_row=z))
            v_i += 1
            i[0].parser(c_table)

    def random_item(self):
        c_list = ""
        c_list += self.name + " "

        if self.Cost:
            c_list += "Cost{ " + str(self.Cost.getRandomCost()) + " }; "

        if self.branchs and self.branchs[0]:
            l = [x[1] for x in self.branchs]
            l = sorted(l, key=fsc.f_sorted_chance)
            number = random.randint(l[0].minChance, l[len(l) - 1].maxChance)
            for x in range(0, len(self.branchs)):
                if (number >= self.branchs[x][1].minChance) and (number <= self.branchs[x][1].maxChance):
                    c_list += str(self.branchs[x][0].random_item()) + " "
                    break

        if self.unique:
            c_list += str(self.unique.get_random_unique()) + " "
        if self.info and self.info[0]:
            for i in self.info:
                c_list += "INFO{ "
                if (i is not str) and (len(i) > 0):
                    for x in i:
                        if x != "":
                            c_list += str(x) + ' '
                c_list += "};"
        return c_list

    def get_mask(self):
        if self.Mask is not None:
            s = ""
            for i in self.Mask:
                s += str(i) + ' '
            return s
        else:
            return "Not Have Mask"
