# -*- coding: UTF-8 -*-
from snownlp import SnowNLP

s = SnowNLP(u'这个东西真心很赞')
s.words
s.sentiments
s.pinyin
s = SnowNLP('这个东西超级差，简直就是垃圾')
s.sentiments
s.tags
print(s.sentiments)
import pymysql

conn = pymysql.connect(host='106.14.33.228', port=3306, user='root', passwd='645540', db='company_spider',
                       charset='utf8')
cur = conn.cursor()
cur.execute("SELECT detailId,commentValue FROM tbcompanydetail")

mconn = pymysql.connect(host='121.42.157.110', port=3306, user='wts', passwd='WeiTS905153840@@', db='test',
                        charset='utf8')

for r in cur.fetchall():
    if r[0] > 10461:
        s = SnowNLP(r[1])
        mcur = mconn.cursor()
        #    a =  str(r[0]) + "," + r[1] + "," + str(s.sentiments) + "," + ('，'.join(s.words))
        #    print(a)

        sql = "INSERT INTO commentsanalysis (`Id`,`CommentValue`,`Positive`,`Words`) VALUES ('%s','%s','%s','%s')" % (
        str(r[0]), r[1], str(s.sentiments), '，'.join(s.words))

        print(sql)

        #    mcur.execute("INSERT INTO commentsanalysis (`Id`,`CommentValue`,`Positive`,`Words`) VALUES (%s,%s,%s,%s)"%(str(r[0]),str(r[1]),str(s.sentiments),'，'.join(s.words)))
        #    mconn.commit()
        try:
            mcur.execute(sql)
            mconn.commit()
            print("success")
        except:
            mconn.rollback()
            print("error")
        print(mcur.Error())

    #    print(r[0])
    #    for q in r:
    #          print(q)

cur.close()
conn.close()

# cur.execute("SELECT detailId,commentValue FROM tbcompanydetail")




