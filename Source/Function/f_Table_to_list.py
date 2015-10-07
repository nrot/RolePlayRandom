__author__ = 'nrot'

import xlrd


def table_to_list(PathToTable):
    table = xlrd.open_workbook(PathToTable, encoding_override="utf-8")
    sheet = table.sheet_by_index(0)
    need_list = []
    for rownum in range(sheet.nrows):
        need_list.append(sheet.row_values(rownum))
    return need_list
