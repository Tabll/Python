import pandas as pd
import os
import numpy


def csv_reader(filename):
    data = pd.read_csv(filename, header=None)
    return data


# Feature Index 1
# The number of black pixels in the image
def get_nr_pix(data):
    count = 0
    for index, row in data.iterrows():
        for i in row:
            if i == 1:
                count += 1
    # print('Index 1: ' + str(count))
    return count


# Feature Index 2
# Number of rows containing at least one black pixel
def get_height(data):
    count = 0
    temp_count = 0
    for index, row in data.iterrows():
        for i in row:
            if i == 1:
                temp_count += 1
        if temp_count != 0:
            count += 1
            temp_count = 0
    # print('Index 2: ' + str(count))
    return count


# Feature Index 3
# Number of columns containing at least one black pixel
def get_width(data):
    count = 0
    temp_count = 0
    transposed_data = numpy.transpose(data)
    # print(transposed_data)
    for index, row in transposed_data.iterrows():
        for i in row:
            if i == 1:
                temp_count += 1
        if temp_count != 0:
            count += 1
            temp_count = 0
    # print('Index 3: ' + str(count))
    return count


# Feature Index 4
# Ratio of height to width; i.e. feature 2 / divided by feature 3
def get_tallness(height, width):
    return height/width


# Feature Index 5
# Number of rows with exactly one black pixel
def get_rows_with_1(data):
    count = 0
    temp_count = 0
    for index, row in data.iterrows():
        for i in row:
            if i == 1:
                temp_count += 1
        if temp_count == 1:
            count += 1
        temp_count = 0
    print('Index 5: ' + str(count))
    return count


# Feature Index 6
# Number of columns with exactly one black pixel
def get_cols_with_1(data):
    count = 0
    temp_count = 0
    transposed_data = numpy.transpose(data)
    for index, row in transposed_data.iterrows():
        for i in row:
            if i == 1:
                temp_count += 1
        if temp_count == 1:
            count += 1
        temp_count = 0
    print('Index 6: ' + str(count))
    return count


# Feature Index 7
# Number of rows with five or more black pixels
def get_rows_with_5_plus(data):
    count = 0
    temp_count = 0
    for index, row in data.iterrows():
        for i in row:
            if i == 1:
                temp_count += 1
        if temp_count >= 5:
            count += 1
        temp_count = 0
    print('Index 7: ' + str(count))
    return count


# Feature Index 8
# Number of columns with five or more black pixels
def get_cols_with_5_plus(data):
    count = 0
    temp_count = 0
    transposed_data = numpy.transpose(data)
    for index, row in transposed_data.iterrows():
        for i in row:
            if i == 1:
                temp_count += 1
        if temp_count >= 5:
            count += 1
        temp_count = 0
    print('Index 8: ' + str(count))
    return count


# Feature Index 9
# Number of black pixels with exactly 1 neighbouring pixel
def get_1neigh(data):
    count = 0
    for index, row in data.iterrows():
        for col_index in data.columns:
            if row[col_index] == 1:
                if numpy.sum(get_neighbouring_pixels(data, col_index, index)) - 1 == 1:
                    count += 1
    print('Index 9: ' + str(count))
    return count


# Feature Index 10
# Number of black pixels with 3 or more neighbours
def get_3_plus_neigh(data):
    count = 0
    for index, row in data.iterrows():
        for col_index in data.columns:
            if row[col_index] == 1:
                if numpy.sum(get_neighbouring_pixels(data, col_index, index)) - 1 >= 3:
                    count += 1
    print('Index 10: ' + str(count))
    return count


# Feature Index 11
# Number of black pixels with no neighbours in the lower-left, lower, or lower-right positions
def get_none_below(data):
    count = 0
    for index, row in data.iterrows():
        for col_index in data.columns:
            if row[col_index] == 1:
                neighbour = get_neighbouring_pixels(data, col_index, index)
                if neighbour[0][2] + neighbour[0][1] + neighbour[0][0] == 0:
                    count += 1
    print('Index 11: ' + str(count))
    return count


# Feature Index 12
# Number of black pixels with no neighbours in the upper-left, upper, or upper-right positions
def get_none_above(data):
    count = 0
    for index, row in data.iterrows():
        for col_index in data.columns:
            if row[col_index] == 1:
                neighbour = get_neighbouring_pixels(data, col_index, index)
                if neighbour[2][2] + neighbour[2][1] + neighbour[2][0] == 0:
                    count += 1
    print('Index 12: ' + str(count))
    return count


# Feature Index 13
# Number of black pixels with no neighbours in the upper-left, left, or lower-left positions
def get_none_before(data):
    count = 0
    for index, row in data.iterrows():
        for col_index in data.columns:
            if row[col_index] == 1:
                neighbour = get_neighbouring_pixels(data, col_index, index)
                if neighbour[0][0] + neighbour[1][0] + neighbour[2][0] == 0:
                    count += 1
    print('Index 13: ' + str(count))
    return count


# Feature Index 14
# Number of black pixels with no neighbours in the upper-right, right, or lower-right positions
def get_none_after(data):
    count = 0
    for index, row in data.iterrows():
        for col_index in data.columns:
            if row[col_index] == 1:
                neighbour = get_neighbouring_pixels(data, col_index, index)
                if neighbour[0][2] + neighbour[1][2] + neighbour[2][2] == 0:
                    count += 1
    print('Index 14: ' + str(count))
    return count


# Feature Index 15
# Feature Index 16
# Feature Index 17
# Feature Index 18
# Feature Index 19
# Feature Index 20


def get_neighbouring_pixels(data, column, row):
    data_column = data.shape[0]
    data_row = data.shape[1]
    neighbour = numpy.zeros((3, 3))
    if column - 1 >= 0:
        neighbour[1][0] = data[column - 1][row]
        if row - 1 >= 0:
            neighbour[0][0] = data[column - 1][row - 1]
        if row + 1 <= data_row - 1:
            neighbour[2][0] = data[column - 1][row + 1]
    if column - 1 >= 0:
        neighbour[0][1] = data[column][row - 1]
    if column + 1 <= data_row - 1:
        neighbour[2][1] = data[column][row + 1]
    if column + 1 <= data_column - 1:
        neighbour[1][2] = data[column + 1][row]
        if row - 1 >= 0:
            neighbour[0][2] = data[column + 1][row - 1]
        if row + 1 <= data_row:
            neighbour[2][2] = data[column + 1][row + 1]
    neighbour[1][1] = data[column][row]
    # print(neighbour)
    return neighbour


def feature_all_data(from_lo, to_lo):
    files = os.listdir(from_lo)
    for file in files:
        data = csv_reader(from_lo + "\\" + file)

    return True


temp = csv_reader("D:\\Projects\\Pythons\\Data\\CSC-3060\\CSV file\\40250516_11_1.csv")
get_nr_pix(temp)
get_height(temp)
get_width(temp)
print(get_tallness(get_height(temp), get_width(temp)))
get_rows_with_1(temp)
get_cols_with_1(temp)
get_rows_with_5_plus(temp)
get_cols_with_5_plus(temp)
get_1neigh(temp)
# get_neighbouring_pixels(temp, 9, 4)
get_3_plus_neigh(temp)
get_none_below(temp)
get_none_above(temp)
get_none_before(temp)
get_none_after(temp)
