#!/usr/bin/evn python3
# coding=utf-8

import mysql.connector

CREATE_SQL='create table user (id varchar(20) primary key, name varchar(20))'
INSERT_SQL='insert into user (id, name) values (%s, %s)'
SELECT_SQL = 'select * from user where id = %s'

def create(cursor):

    cursor.execute(CREATE_SQL)

conn = mysql.connector.connect(user='root',password='root',database='test')
cursor = conn.cursor()
# create(cursor)

cursor.execute(INSERT_SQL,['1','AAA'])
print(cursor.rowcount)
conn.commit()

cursor.execute(SELECT_SQL, ['1'])
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()
