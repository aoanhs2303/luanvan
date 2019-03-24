import pymysql.cursors
import DataStructure as DS

conn1 = pymysql.connect(host='127.0.0.1', user='root', password='root', db='mydata')
conn2 = pymysql.connect(host='127.0.0.1', user='root', password='root', db='mydata')

List_EntityInfo = list()

cursor1 = conn1.cursor()
cursor2 = conn2.cursor()

sql1 = "SELECT DISTINCT gender FROM customer"
cursor1.execute(sql1)
for row in cursor1:
    EI = DS.EntityInfo(row[0].lower(), list())
    sql2 = "SELECT DISTINCT customer_id FROM customer WHERE gender = %s"
    cursor2.execute(sql2, row[0])
    listE = list()
    for row2 in cursor2:
        listE.append(row2[0])
    LE = {"gender": listE}
    EI.listRelationsAndEntities.append(LE)
    List_EntityInfo.append(EI)


cursor1 = conn1.cursor()
cursor2 = conn2.cursor()

sql = "SELECT DISTINCT city FROM customer"
cursor1.execute(sql)
for row in cursor1:
    EI = DS.EntityInfo(row[0], list())
    sql2 = "SELECT DISTINCT customer_id FROM customer WHERE city = %s"
    cursor2.execute(sql2, row[0])
    listE = list()
    for row2 in cursor2:
        listE.append(row2[0])
    LE = {"city": listE}
    EI.listRelationsAndEntities.append(LE)
    List_EntityInfo.append(EI)


cursor1 = conn1.cursor()
cursor2 = conn2.cursor()

sql1 = "SELECT DISTINCT marital_status FROM customer"
cursor1.execute(sql1)
for row in cursor1:
    EI = DS.EntityInfo(row[0], list())
    sql2 = "SELECT DISTINCT customer_id FROM customer WHERE marital_status = %s"
    cursor2.execute(sql2, row[0])
    listE = list()
    for row2 in cursor2:
        listE.append(row2[0])
    LE = {"marital status": listE}
    EI.listRelationsAndEntities.append(LE)
    List_EntityInfo.append(EI)


cursor1 = conn1.cursor()
cursor2 = conn2.cursor()
sql1 = "SELECT DISTINCT customer_id FROM customer"
cursor1.execute(sql1)
for row in cursor1:
    EI = DS.EntityInfo(row[0], list())
    List_EntityInfo.append(EI)


cursor1 = conn1.cursor()
cursor2 = conn2.cursor()

sql1 = "SELECT DISTINCT brand_name FROM product"
cursor1.execute(sql1)
for row in cursor1:
    EI = DS.EntityInfo(row[0], list())
    sql2 = "SELECT DISTINCT product_id FROM product WHERE brand_name = %s"
    cursor2.execute(sql2, row[0])
    listE = list()
    for row2 in cursor2:
        listE.append(row2[0])
    LE = {"brand name": listE}
    EI.listRelationsAndEntities.append(LE)
    List_EntityInfo.append(EI)


cursor1 = conn1.cursor()
cursor2 = conn2.cursor()

sql1 = "SELECT DISTINCT low_fat FROM product"
cursor1.execute(sql1)
for row in cursor1:
    EI = DS.EntityInfo(row[0], list())
    sql2 = "SELECT DISTINCT product_id FROM product WHERE low_fat = %s"
    cursor2.execute(sql2, int(row[0]))
    listE = list()
    for row2 in cursor2:
        listE.append(row2[0])
    LE = {"low fat": listE}
    EI.listRelationsAndEntities.append(LE)
    List_EntityInfo.append(EI)


cursor1 = conn1.cursor()
cursor2 = conn2.cursor()
sql1 = "SELECT DISTINCT product_id FROM _order"
cursor1.execute(sql1)
for row in cursor1:
    EI = DS.EntityInfo(row[0], list())
    sql2 = "SELECT DISTINCT customer_id FROM _order WHERE product_id = %s"
    cursor2.execute(sql2, int(row[0]))
    listE = list()
    for row2 in cursor2:
        listE.append(row2[0])
    LE = {"buy": listE}
    EI.listRelationsAndEntities.append(LE)
    List_EntityInfo.append(EI)

print('done entity info!')
