import Config
import GenerateItemChains as GIC
import Generate2LargeItemChains as G2LIC
import GenerateRules as GR
import Helper
import datetime
import pymysql.cursors
import DataStructure as DS


def MRAR():
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
            listE.append("c_" + str(row2[0]))
        LE = {"gender": listE}
        EI.listRelationsAndEntities.append(LE)
        List_EntityInfo.append(EI)

    cursor1 = conn1.cursor()
    cursor2 = conn2.cursor()

    cus = 0
    sql = "SELECT DISTINCT city FROM customer"
    cursor1.execute(sql)
    for row in cursor1:
        cus += 1
        EI = DS.EntityInfo(row[0], list())
        sql2 = "SELECT DISTINCT customer_id FROM customer WHERE city = %s"
        cursor2.execute(sql2, row[0])
        listE = list()
        for row2 in cursor2:
            listE.append("c_" + str(row2[0]))
        LE = {"city": listE}
        EI.listRelationsAndEntities.append(LE)
        List_EntityInfo.append(EI)

    print(cus)
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
            listE.append("c_" + str(row2[0]))
        LE = {"marital status": listE}
        EI.listRelationsAndEntities.append(LE)
        List_EntityInfo.append(EI)

    cursor1 = conn1.cursor()
    cursor2 = conn2.cursor()
    sql1 = "SELECT DISTINCT customer_id FROM customer"
    cursor1.execute(sql1)
    for row in cursor1:
        EI = DS.EntityInfo("c_" + str(row[0]), list())
        List_EntityInfo.append(EI)

    # cursor1 = conn1.cursor()
    # cursor2 = conn2.cursor()
    #
    # sql1 = "SELECT DISTINCT brand_name FROM product"
    # cursor1.execute(sql1)
    # for row in cursor1:
    #     EI = DS.EntityInfo(row[0], list())
    #     sql2 = "SELECT DISTINCT product_id FROM product WHERE brand_name = %s"
    #     cursor2.execute(sql2, row[0])
    #     listE = list()
    #     for row2 in cursor2:
    #         listE.append(row2[0])
    #     LE = {"brand name": listE}
    #     EI.listRelationsAndEntities.append(LE)
    #     List_EntityInfo.append(EI)

    # cursor1 = conn1.cursor()
    # cursor2 = conn2.cursor()
    #
    # sql1 = "SELECT DISTINCT low_fat FROM product"
    # cursor1.execute(sql1)
    # for row in cursor1:
    #     EI = DS.EntityInfo(True if row[0] == 1 else False, list())
    #     sql2 = "SELECT DISTINCT product_id FROM product WHERE low_fat = %s"
    #     cursor2.execute(sql2, int(row[0]))
    #     listE = list()
    #     for row2 in cursor2:
    #         listE.append(row2[0])
    #     LE = {"low fat": listE}
    #     EI.listRelationsAndEntities.append(LE)
    #     List_EntityInfo.append(EI)

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
            listE.append("c_" + str(row2[0]))
        LE = {"buy": listE}
        EI.listRelationsAndEntities.append(LE)
        List_EntityInfo.append(EI)

    print('done entity info!')

    Map_EntityInfo = dict()
    for EntityInfo in List_EntityInfo:
        Map_EntityInfo[EntityInfo.endPointEntity] = EntityInfo.listRelationsAndEntities

    LLICs = []
    AllCandidate = []

    for EntityInfo in List_EntityInfo:
        for Relation in EntityInfo.listRelationsAndEntities:
            r = list(Relation.keys())[0]
            e = Relation.get(r)
            GIC.GenerateItemChains(EntityInfo.endPointEntity, r, e, 1, LLICs, Map_EntityInfo)

    ItemChains = LLICs.copy()
    AllCandidate.append(list())
    AllCandidate.append(ItemChains)

    LLICs = G2LIC.Generate2LargeItemChains(LLICs)
    AllCandidate.append(LLICs.copy())
    print("Done 2 LargeIC")
    L = 0
    while L < len(LLICs):
        L = L + 1
        ICs = list()
        lengthOfArray = len(LLICs)
        print(lengthOfArray)
        for i in range(lengthOfArray):
            for j in range(i + 1, lengthOfArray - 1):
                if LLICs[i].List_Of_ChainIDs[:L] == LLICs[j].List_Of_ChainIDs[:L]:
                    largeIC = Helper.CombineAndSort(LLICs[i], LLICs[j], L)
                    if largeIC is not None:
                        ICs.append(largeIC)
        LLICs = ICs
        AllCandidate.append(ICs)
    Rules = GR.GenerateRule(AllCandidate)
    Helper.writeRule2File(Rules, ItemChains)
    return Rules


if __name__ == '__main__':
    start = datetime.datetime.now()
    rules = MRAR()
    print(len(rules))
    end = datetime.datetime.now()
    print(end - start)
