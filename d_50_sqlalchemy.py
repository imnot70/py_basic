#!/usr/bin/env python3
# coding=utf-8

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import inspect,mysql.connector

CONN_URL='mysql+mysqlconnector://root:root@localhost:3306/test'

# 创建对象的基类:
Base = declarative_base()

class User(Base):
    # 表的名字:
    __tablename__ = 'user'
    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

engine = create_engine(CONN_URL)
