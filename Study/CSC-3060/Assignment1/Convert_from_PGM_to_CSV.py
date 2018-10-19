# import re
# import numpy
import numpy as np
# from PIL import Image
# import os, glob


def pgm_reader(name):
    with open(name) as filename:
        lines = filename.readlines()
    # Ignores commented lines
    for l in list(lines):
        if l[0] == '#':
            lines.remove(l)
    assert lines[0].strip() == 'P2'  # 确保字符编码是 ASCII (P2)
    data = []
    for line in lines[1:]:
        data.extend([int(c) for c in line.split()])   # Read Data
    return np.array(data[3:]), (data[1], data[0]), data[2]


def convert_pgm_data(pgm_array):
    size = pgm_array[1]
    data = pgm_array[0]
    new_data = np.zeros((size[0], size[1]))
    temp_index = 1
    row = 0
    column = 0
    for number in data:
        if number == 255:
            number = 1
        new_data[row][column] = number
        column += 1
        if temp_index % size[0] == 0 and temp_index != 0:
            column = 0
            row += 1
        temp_index += 1
    return new_data


pgm_data = pgm_reader("D:\\Projects\\Pythons\\Data\\CSC-3060\\PGM file\\2-1.pgm")  # 返回的pgm_data[0]是数据
# print(pgm_data[0][21])
new = convert_pgm_data(pgm_data)
print(new)
# exit()
