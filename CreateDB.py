#! /usr/bin/python
import pymysql.cursors

connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='root',
                             db='dataset')

print("connect successful!!")

connection2 = pymysql.connect(host='127.0.0.1',
                              user='root',
                              password='root',
                              db='mydata')

try:

    # create table
    with connection2.cursor() as cursor:
        sql = "CREATE TABLE `customer` (`customer_id` INT(11) NOT NULL,`city` VARCHAR(30) NULL,`marital_status` VARCHAR(30) NULL,`gender` VARCHAR(30) NULL,PRIMARY KEY (`customer_id`));"
        # commit; ;
        cursor.execute(sql)
        print('create table customer: done!')

        sql = " CREATE TABLE `product` (`product_id` INT(11) NOT NULL,`brand_name` VARCHAR(60) NULL,`low_fat` TINYINT(1) NULL,PRIMARY KEY (`product_id`));"

        cursor.execute(sql)
        print('create table product: done!')

        sql = "CREATE TABLE `_order` (`customer_id` INT(11) NULL,`product_id` INT(11) NULL,INDEX `fk_customer_id_idx` (`customer_id` ASC),INDEX `fk_product_id_idx` (`product_id` ASC),CONSTRAINT `fk_customer_id`FOREIGN KEY (`customer_id`)REFERENCES `mydata`.`customer` (`customer_id`) ON DELETE CASCADE ON UPDATE RESTRICT, CONSTRAINT `fk_product_id` FOREIGN KEY (`product_id`) REFERENCES `mydata`.`product` (`product_id`) ON DELETE CASCADE ON UPDATE RESTRICT);"
        cursor.execute(sql)
        print('create table _oder: done!')

        connection2.commit()
    # import customer
    with connection.cursor() as cursor:
        # SQL
        sql = "SELECT * from customer"
        cursor.execute(sql)
        for row in cursor:
            with connection2.cursor() as cursor2:
                sql = "INSERT INTO `customer` (`customer_id`, `city`, `marital_status`, `gender`) VALUE (%s, %s, %s, %s)"
                cursor2.execute(sql, (int(row[0]), row[9], row[17], row[19]))
            # print(row[0] ,row[9], row[17], row[19])
        connection2.commit()
        print('add customer: done!')

    # import product
    with connection.cursor() as cursor:
        # SQL
        sql = "SELECT * from product"
        cursor.execute(sql)
        for row in cursor:
            with connection2.cursor() as cursor2:
                sql = "INSERT INTO `product` (`product_id`, `brand_name`, `low_fat`) VALUE (%s, %s, %s)"
                cursor2.execute(sql, (int(row[1]), row[2], int(row[9])))
            # print(row[1] ,row[2], row[9])
        connection2.commit()
        print('add product: done!')

    # import order
    with connection.cursor() as cursor:
        # SQL
        sql = "SELECT * from agg_c_special_sales_fact_1997"
        cursor.execute(sql)
        for row in cursor:
            with connection2.cursor() as cursor2:
                sql = "INSERT INTO `_order` (`product_id`, `customer_id`) VALUE (%s, %s)"
                cursor2.execute(sql, (int(row[0]), int(row[2])))
            # print(row[0] ,row[2])
        connection2.commit()
        print('add order: done!')

finally:
    connection.close()
    connection2.close()