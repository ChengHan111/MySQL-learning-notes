# find all data in form info in database person
# 1
import pymysql
# 2
try:
    # Using ctrl + B to find the usage of Connect
    connc = pymysql.Connect(
        host= '127.0.0.1', #real ip(ifconfig ens33's ip) or localhost or 127.0.0.1
        user='root',
        password="",
        database="person",
        port=3306,
        charset='utf8')
# 3
    cur = connc.cursor()
# 4 sql languages
    sql = 'select*from info;'
# 5 use cur in order to use sql
    cur.execute(sql)
# 6 output
    result = cur.fetchall()
    print(result)
# 7
    cur.close()
# 8
    connc.close()

#     Noticing that I am not using commit in this section since nothing has changed to my database
#     But the truth is when u are about to change your database, u need to commit the changes or the changes wont be saved in database
#  Using try/ exception to find the error of database
except Exception as e:
    print(e)
