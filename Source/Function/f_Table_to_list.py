__author__ = 'nrot'

import xlrd

def Table_to_list(PathToTable):
    table = xlrd.open_workbook(PathToTable, encoding_override="utf-8")
    sheet = table.sheet_by_index(0)
    needList = []
    for rownum in range(sheet.nrows):
        needList.append(sheet.row_values(rownum))
    return needList