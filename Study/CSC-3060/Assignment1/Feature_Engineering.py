import pandas as pd
import os
import numpy


# The reader of the csv
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
    # print('Index 5: ' + str(count))
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
    # print('Index 6: ' + str(count))
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
    # print('Index 7: ' + str(count))
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
    # print('Index 8: ' + str(count))
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
    # print('Index 9: ' + str(count))
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
    # print('Index 10: ' + str(count))
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
    # print('Index 11: ' + str(count))
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
    # print('Index 12: ' + str(count))
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
    # print('Index 13: ' + str(count))
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
    # print('Index 14: ' + str(count))
    return count


# Feature Index 15
# This feature has the number of connected regions in the image
def get_nr_regions(data):
    count = 0
    region = numpy.zeros((data.shape[1], data.shape[0]))
    for index, row in data.iterrows():
        for col_index in data.columns:
            if row[col_index] == 1 and region[index][col_index] == 0:
                count += 1
                region = mark_region(data, region, index, col_index, count)
                # print(region)
                # neighbour = get_neighbouring_pixels(data, col_index, index)
                # if numpy.sum(neighbour) >= 2:
    # print('Index 15: ' + str(count))
    return count


# Feature Index 16
# This feature is the number of eyes in the image
def get_nr_eyes(data):
    count = 0
    # print(data)
    eye_counter = 0
    eye = numpy.zeros((data.shape[1], data.shape[0]))
    for index, row in data.iterrows():
        for col_index in data.columns:
            if row[col_index] == 1 and eye[index][col_index] == 0:
                starter = [index, col_index]
                count += 1
                [eye, eye_counter] = is_eye(data, eye, index, col_index, count, starter, 0)
                # print(eye_counter)
                # neighbour = get_neighbouring_pixels(data, col_index, index)
                # if numpy.sum(neighbour) >= 2:
    count -= 1
    # print('Index 16: ' + str(eye_counter))
    return count


# Feature Index 17
# Number of rows with at least five black pixels) minus (number of columns with at least five black pixels
def get_r5_c5(data):
    return get_rows_with_5_plus(data) - get_cols_with_5_plus(data)


# Feature Index 18
# Design your own feature which you think may be useful for distinguishing between "b" and "d" character images.
def get_bd(data):
    [max_width, min_width, max_height, min_height] = max_min_width_height(data)
    # print(str(max_width) + "," + str(min_width) + "," + str(max_height) + "," + str(min_height))
    center_width = (max_width + min_width)/2
    center_height = (max_height + min_height)/2
    # print(str(center_width) + "," + str(center_height))

    [average_width, average_height] = average_width_height(data)
    # print(str(average_width) + "," + str(average_height))
    # print('Index 18: ' + str(average_width - center_width))
    # print(average_height - center_height)
    count = 0
    # for index, row in data.iterrows():
    #     for col_index in data.columns:
    #         count
    return average_width - center_width


# Feature Index 19
def get_max_neighbour(data):
    max_neighbour = 0
    for index, row in data.iterrows():
        for col_index in data.columns:
            if row[col_index] == 1:
                neighbour = get_neighbouring_pixels(data, col_index, index)
                su = numpy.sum(neighbour)
                if su > max_neighbour:
                    max_neighbour = su
    # print('Index 19: ' + str(max_neighbour))
    return max_neighbour


# Feature Index 20
def get_black_in_every_line(data):
    all_black_number = 0
    for index, row in data.iterrows():
        for col_index in data.columns:
            if data[col_index][index] == 1:
                all_black_number += 2
    black_in_every_line = all_black_number/(get_width(data) + get_height(data))
    # print('Index 20: ' + str(black_in_every_line))
    return black_in_every_line


def average_width_height(data):
    point_count = 0
    width_sum = 0
    height_sum = 0
    for index, row in data.iterrows():
        for col_index in data.columns:
            if data[col_index][index] == 1:
                point_count += 1
                width_sum += col_index
                height_sum += index
    if point_count == 0:
        point_count = 1
    return [width_sum/point_count, height_sum/point_count]


def max_min_width_height(data):
    max_width = 0
    min_width = data.shape[1]
    max_height = 0
    min_height = data.shape[0]
    for index, row in data.iterrows():
        for col_index in data.columns:
            if data[col_index][index] == 1:
                # print(index)
                # print(col_index)
                if index > max_height:
                    max_height = index
                if index < min_height:
                    min_height = index
                if col_index > max_width:
                    max_width = col_index
                if col_index < min_width:
                    min_width = col_index
    return [max_width, min_width, max_height, min_height]


def is_eye(data, eye, row, column, count, starter, eye_counter):
    eye[row][column] = count
    neighbour = get_neighbouring_pixels(data, column, row)
    # [n_rows, n_cols] = neighbour.shape
    # print(n_rows, n_cols)
    for i in range(neighbour.shape[0]):
        for j in range(neighbour.shape[1]):
            if starter == [j + column - 1, i + row - 1]:
                eye_counter += 1
                # print("Find!" + str(column) + " " + str(row))
            if 1 <= i + row <= data.shape[0] and 1 <= j + column <= data.shape[1]:
                if neighbour[i][j] == 1 \
                        and (i != 1 or j != 1) \
                        and eye[i + row - 1][j + column - 1] == 0:
                        if 1 <= i + row <= data.shape[0] and 1 <= j + column <= data.shape[1]:
                            [eye, eye_counter] = is_eye(data, eye, i + row - 1, j + column - 1, count, starter, eye_counter)
                # print(neighbour[i, j])
    # for index, n_row in neighbour:
    #     for col_index in neighbour.columns:
    #         if neighbour[index][col_index] == 1 \
    #                 and (index != 1 or col_index != 1) \
    #                 and region[index + row - 1][col_index + column - 1] != 0:
    #             region = mark_region(data, region, index + row - 1, col_index + column - 1, count)
    return [eye, eye_counter]


def mark_region(data, region, row, column, count):
    region[row][column] = count
    neighbour = get_neighbouring_pixels(data, column, row)

    [n_rows, n_cols] = neighbour.shape
    # print(n_rows, n_cols)
    for i in range(n_rows):
        for j in range(n_cols):
            if neighbour[i][j] == 1 \
                    and (i != 1 or j != 1) \
                    and region[i + row - 1][j + column - 1] == 0:
                if 1 <= i + row <= data.shape[0] and 1 <= j + column <= data.shape[1]:
                    region = mark_region(data, region, i + row - 1, j + column - 1, count)
            # print(neighbour[i, j])
    # for index, n_row in neighbour:
    #     for col_index in neighbour.columns:
    #         if neighbour[index][col_index] == 1 \
    #                 and (index != 1 or col_index != 1) \
    #                 and region[index + row - 1][col_index + column - 1] != 0:
    #             region = mark_region(data, region, index + row - 1, col_index + column - 1, count)
    return region


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
    if row - 1 >= 0:
        neighbour[0][1] = data[column][row - 1]
    if row + 1 <= data_row - 1:
        neighbour[2][1] = data[column][row + 1]
    if column + 1 <= data_column - 1:
        neighbour[1][2] = data[column + 1][row]
        if row - 1 >= 0:
            neighbour[0][2] = data[column + 1][row - 1]
        if row + 1 <= data_row - 1:
            neighbour[2][2] = data[column + 1][row + 1]
    neighbour[1][1] = data[column][row]
    # print(neighbour)
    return neighbour


def get_label_and_index(file_name: str):
    strings = file_name.split("_", 2)
    strings[2] = strings[2].split(".", 1)[0]
    # print(strings)
    return [strings[1], strings[2]]


def feature_all_data(from_lo, to_lo):
    files = os.listdir(from_lo)
    file_counter = 0
    feature_data = numpy.zeros((168, 22))
    for file in files:
        [label, index] = get_label_and_index(file)
        data = csv_reader(from_lo + "\\" + file)

        feature_data[file_counter][0] = label
        feature_data[file_counter][1] = index

        feature_data[file_counter][2] = get_nr_pix(data)
        feature_data[file_counter][3] = get_height(data)
        feature_data[file_counter][4] = get_width(data)
        feature_data[file_counter][5] = get_tallness(get_height(data), get_width(data))
        feature_data[file_counter][6] = get_rows_with_1(data)
        feature_data[file_counter][7] = get_cols_with_1(data)
        feature_data[file_counter][8] = get_rows_with_5_plus(data)
        feature_data[file_counter][9] = get_cols_with_5_plus(data)
        feature_data[file_counter][10] = get_1neigh(data)
        feature_data[file_counter][11] = get_3_plus_neigh(data)
        feature_data[file_counter][12] = get_none_below(data)
        feature_data[file_counter][13] = get_none_above(data)
        feature_data[file_counter][14] = get_none_before(data)
        feature_data[file_counter][15] = get_none_after(data)
        feature_data[file_counter][16] = get_nr_regions(data)
        feature_data[file_counter][17] = get_nr_eyes(data)
        feature_data[file_counter][18] = get_r5_c5(data)
        feature_data[file_counter][19] = get_bd(data)
        feature_data[file_counter][20] = get_max_neighbour(data)
        feature_data[file_counter][21] = get_black_in_every_line(data)

        # print(data)
        file_counter += 1
    print(feature_data)
    data = pd.DataFrame(feature_data)
    data[0] = data[0].astype("int")
    data[1] = data[1].astype("int")
    data[2] = data[2].astype("int")
    data[3] = data[3].astype("int")
    data[4] = data[4].astype("int")
    data[5] = data[5].round(4)
    data[6] = data[6].astype("int")
    data[7] = data[7].astype("int")
    data[8] = data[8].astype("int")
    data[9] = data[9].astype("int")
    data[10] = data[10].astype("int")
    data[11] = data[11].astype("int")
    data[12] = data[12].astype("int")
    data[13] = data[13].astype("int")
    data[14] = data[14].astype("int")
    data[15] = data[15].astype("int")
    data[16] = data[16].astype("int")
    data[17] = data[17].astype("int")
    data[18] = data[18].astype("int")
    data[19] = data[19].round(4)
    data[20] = data[20].astype("int")
    data[21] = data[21].round(4)
    print(data[0])
    print(data)
    data.to_csv(to_lo + "\\" + "40250516_features.csv", header=False, index=False)
    return data


# temp = csv_reader("D:\\Projects\\Pythons\\Data\\CSC-3060\\CSV file\\40250516_33_1.csv")
# get_nr_pix(temp)
# get_height(temp)
# get_width(temp)
# print(get_tallness(get_height(temp), get_width(temp)))
# get_rows_with_1(temp)
# get_cols_with_1(temp)
# get_rows_with_5_plus(temp)
# get_cols_with_5_plus(temp)
# get_1neigh(temp)
# # get_neighbouring_pixels(temp, 9, 4)
# get_3_plus_neigh(temp)
# get_none_below(temp)
# get_none_above(temp)
# get_none_before(temp)
# get_none_after(temp)
# get_nr_regions(temp)
# get_nr_eyes(temp)
# print('Index 17: ' + str(get_r5_c5(temp)))
# get_bd(temp)
# get_max_neighbour(temp)
# get_black_in_every_line(temp)

test = feature_all_data("D:\\Projects\\Pythons\\Data\\CSC-3060\\CSV file",
                        "D:\\Projects\\Pythons\\Data\\CSC-3060\\Features")
