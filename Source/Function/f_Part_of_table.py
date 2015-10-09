__author__ = 'nrot'


def f_part_of_table(table, start_col, stop_col, start_row=None, stop_row=None):
    list = []

    if start_row == None and stop_row == None:
        for i in table:
            z = start_col
            while z <= stop_col:
                list.append(i[z])
                z += 1
    elif start_row == stop_row and start_row != None:
        stop_row = start_row + 1
        x = start_row
        y = start_col
        while x < stop_row:
            y = start_col
            while y < stop_col:
                list.append(table[x][y])
                y += 1
            x += 1
    return list


def f_part_of_list(list, start, stop):
    c_list = []

    for x in range(start, stop):
        c_list.append(list[x])
    return c_list
