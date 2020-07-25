import pymysql
connc = pymysql.Connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="person",
    port=3306,
    charset='utf8')
# 3
cur = connc.cursor()
try:
    # 4 sql languages
    # 4.1.add data
    # sql = 'insert into info values(%s,%s,%s,%s)'
    # add_data = [0,'Dehua Liu',22,'male']

    # 4.2. update data
    # sql = 'update info set Name = %s where id = 14'
    # update_data = ['Lee']

    # 4.3. delete data
    sql = 'delete from info where Name = %s'
    delete_data = ['Dehua Liu']

    # 5 use cur in order to use sql
    # 5.1 add_data
    # cur.execute(sql,add_data)
    # 5.2 update data
    # cur.execute(sql,update_data)
    # 5.3 delete data
    cur.execute(sql,delete_data)
    #! This step is really important when changing the databases,always remember to commit the results
    connc.commit()

except Exception as e:
    print(e)
    # if these actions fail, rollback to original status !!!
    connc.rollback()
    # # 6 output
    # result = cur.fetchall()
    # print(result)
    # 7
finally:
    cur.close()
    # 8
    connc.close()
    print('all over')

