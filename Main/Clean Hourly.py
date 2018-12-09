import pymysql
import datetime
import random
import string

now_time = datetime.datetime.now()
db_read = pymysql.connect(host="10.66.85.250", port=3306, user="data_reader", passwd="Wtsdata456",
                     db="data", charset='utf8')
db_write = pymysql.connect(host="10.66.85.250", port=3306, user="data_saver", passwd="Wtsdata123",
                     db="data", charset='utf8')
new_data_z = {}
new_data_w = {}
c_time = now_time


def get_data():
    cursor = db_read.cursor()
    sql = "SELECT `id`," \
          "`rank`," \
          "`content`," \
          "`heat`," \
          "`source`," \
          "`update_time` " \
          "FROM `now_hour` " \
          "where update_time >= '" + (now_time - datetime.timedelta(hours=1)
                                      - datetime.timedelta(minutes=4)).strftime("%Y-%m-%d %H:%M:%S") + "' " \
          "and update_time <= '" + (now_time - datetime.timedelta(minutes=4)).strftime("%Y-%m-%d %H:%M:%S") + "'"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            content = row[2]
            heat = row[3]
            source = row[4]
            time: datetime.datetime = row[5]
            if source == 'z':
                add_to_dictionary(new_data_z, content, time.minute // 5, heat)
            elif source == 'w':
                add_to_dictionary(new_data_w, content, time.minute // 5, heat)
        return sql
    except():
        return 0


def add_to_dictionary(dictionary, key, t, value):
    if key in dictionary.keys():
        content = dictionary[key]
    else:
        content = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    content[t] = value
    dictionary.update({key: content})


def sql_save(new_id, content, data, heat, source):
    cursor = db_write.cursor()
    sql = "INSERT INTO hourly_history (`id`, `content`, " \
          "`heat_a`, `heat_b`, `heat_c`, `heat_d`, `heat_e`, `heat_f`, " \
          "`heat_g`, `heat_h`, `heat_i`, `heat_j`, `heat_k`, `heat_l`, " \
          "`heat`, `source`, `calculate_time`) VALUES ('" \
          + new_id + "','" \
          + content + "'," \
          + str(data[0]) + "," \
          + str(data[1]) + "," \
          + str(data[2]) + "," \
          + str(data[3]) + "," \
          + str(data[4]) + "," \
          + str(data[5]) + "," \
          + str(data[6]) + "," \
          + str(data[7]) + "," \
          + str(data[8]) + "," \
          + str(data[9]) + "," \
          + str(data[10]) + "," \
          + str(data[11]) + "," \
          + str(heat) + ",'" \
          + source + "','" \
          + str(c_time) + "')"
    try:
        cursor.execute(sql)
    except():
        db_write.rollback()


def save_data():
    for key in new_data_z:
        new_id = ''.join(random.sample(string.ascii_letters + string.digits, 9))
        heat = sum(new_data_z[key])
        sql_save(new_id, key, new_data_z[key], heat, 'z')

    for key in new_data_w:
        new_id = ''.join(random.sample(string.ascii_letters + string.digits, 9))
        heat = sum(new_data_w[key])
        sql_save(new_id, key, new_data_w[key], heat, 'w')


def sql_commit():
    try:
        db_write.commit()
        return True
    except():
        db_write.rollback()
        return False


def sql_clean():
    cursor = db_write.cursor()
    sql = "DELETE FROM now_hour WHERE " \
          "update_time <= '" + (now_time - datetime.timedelta(days=3)
                                - datetime.timedelta(minutes=4)).strftime("%Y-%m-%d %H:%M:%S") + "'"
    try:
        cursor.execute(sql)
        return True
    except():
        db_write.rollback()
        return False


get_data()
save_data()
sql_clean()
sql_commit()
db_read.close()
db_write.close()
