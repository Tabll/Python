import numpy as np
import os
import pandas


def pgm_reader(name):
    with open(name) as filename:
        lines = filename.readlines()
    # Ignores commented lines
    for l in list(lines):
        if l[0] == '#':
            lines.remove(l)
    assert lines[0].strip() == 'P2'  # make sure it have P2(it means it is ASCII) inside
    data = []
    for line in lines[1:]:
        data.extend([int(c) for c in line.split()])   # read the data
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


def convert_all_file(from_lo, to_lo):
    # pgm_data = pgm_reader(from_lo)
    # file_list = []
    files = os.listdir(from_lo)
    for file in files:
        csv_file_name = "40250516" + get_symbol_label_and_number(file) + ".csv"
        # file_list.append(file)
        csv_data = convert_pgm_data(pgm_reader(from_lo + "\\" + file))
        # print(csv_data)
        data = pandas.DataFrame(csv_data)
        data.to_csv(to_lo + "\\" + csv_file_name, header=False, index=False, float_format='%d')
        # np.SaveTxt(to_lo + "\\" + csv_file_name, csv_data, delimiter=',')
        # print(file)
        print("out put success " + csv_file_name)
    print("all finished!")


def get_symbol_label_and_number(file_name: str):
    strings = file_name.split("-", 1)
    return "_" + get_convert_dictionary()[strings[0]] + "_" + strings[1].split(".", 1)[0]


def get_convert_dictionary():
    return {'1': '11',
            '2': '12',
            '3': '13',
            '4': '14',
            '5': '15',
            '6': '16',
            '7': '17',
            'a': '21',
            'b': '22',
            'c': '23',
            'd': '24',
            'e': '25',
            'f': '26',
            'g': '27',
            'smaller': '31',
            'bigger': '32',
            'equal': '33',
            'se': '34',
            'be': '35',
            'unequal': '36',
            'ae': '37',
            }


convert_all_file("D:\\Projects\\Pythons\\Data\\CSC-3060\\PGM file", "D:\\Projects\\Pythons\\Data\\CSC-3060\\CSV file")
