__author__ = 'nrot'

# -*- coding: utf-8 -*-

import xlrd

class Type_table(object):
    def __init__(self, inpath):
        try:
            self.File = xlrd.open_workbook(inpath)
            self.Sheet = self.File.sheet_by_index(0)
        except:
            self.Error = "All very bad"