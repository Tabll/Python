import requests
from bs4 import BeautifulSoup
import json
import pymysql
import random
import string

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
data = {
    'cate': 'realtimehot'
}
db = pymysql.connect(host="10.66.85.250", port=3306, user="data_saver", passwd="Wtsdata123",
                     db="data", charset='utf8')


def get_weibo():
    try:
        r = requests.get('https://s.weibo.com/top/summary?', params=data, headers=headers)
        # print(r.url)
        if r.status_code == 200:
            html = r.text
        else:
            html = ""
    except():
        html = ""
    soup = BeautifulSoup(html, 'lxml')
    sc = soup.find_all('td', attrs={'class': 'td-02'})
    counter = 1
    sc.remove(sc[0])
    if len(sc) == 50:
        sql_clean('w')
        for main_data in sc:
            c = str(main_data).split(">")
            content = c[2].split("<")[0]
            heat = int(1.07 ** (50 - counter))
            salt = ''.join(random.sample(string.ascii_letters + string.digits, 9))
            print(salt + str(counter) + content + str(heat))
            sql_save(salt, str(counter), content, str(heat), 'w')
            counter += 1


def get_zhihu():
    res = requests.get('https://www.zhihu.com/api/v3/feed/topstory/hot-list-web?limit=50&desktop=true', headers=headers)
    m = json.loads(res.text)
    counter = 1
    if len(m['data']) == 50:
        sql_clean('z')
        for c in m['data']:
            content = c['target']['title_area']['text']
            heat = int(1.07 ** (50 - counter))
            salt = ''.join(random.sample(string.ascii_letters + string.digits, 9))
            print(salt + str(counter) + content + str(heat))
            sql_save(salt, str(counter), content, str(heat), 'z')
            counter += 1


def sql_save(this_id, rank, content, heat, source):
    cursor = db.cursor()
    sql = "INSERT INTO now (`id`,`rank`, `content`, `heat`, `source`) VALUES ('" \
          + this_id + "'," \
          + rank + ",'" \
          + content + "'," \
          + heat + ",'" \
          + source + "')"
    sql_hour = "INSERT INTO now_hour (`id`,`rank`, `content`, `heat`, `source`) VALUES ('" \
          + this_id + "'," \
          + rank + ",'" \
          + content + "'," \
          + heat + ",'" \
          + source + "')"
    try:
        cursor.execute(sql)
        cursor.execute(sql_hour)
    except():
        db.rollback()


def sql_clean(source):
    cursor = db.cursor()
    sql = "DELETE FROM now WHERE `source` = '" + source + "'"
    try:
        cursor.execute(sql)
        return True
    except():
        db.rollback()
        return False


def sql_commit():
    try:
        db.commit()
        return True
    except():
        db.rollback()
        return False


get_weibo()
get_zhihu()

sql_commit()
db.close()
