#!/usr/bin/env python3
# coding=utf-8

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

CONN_URL='mysql+mysqlconnector://root:root@localhost:3306/test'

Base = declarative_base()
engine = create_engine(CONN_URL)
# 创建 DBSession 类型:
DBSession = sessionmaker(bind=engine)

class User(Base):
    # 表的名字:
    __tablename__ = 'user'
    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 创建 Session:
session = DBSession()
# 创建 Query 查询，filter 是 where 条件，
# 最后调用 one()返回唯一行，如果调用 all()则返回所有行:
user = session.query(User).filter(User.id=='5').one()
# 打印类型和对象的 name 属性:
print('type:', type(user))
print('name:', user.name)
# 关闭 Session:
session.close()