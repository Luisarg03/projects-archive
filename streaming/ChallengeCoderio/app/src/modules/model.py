#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import Column, DateTime, ForeignKey, Integer, Float, String, Text
from sqlalchemy.orm import relationship ### Try
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base


def model_create(engine_db):
    '''
    Create tables model IN DB

    Parameters
    ----------
    engine : sqlalchemy engine
        engine db
    
    Returns
    ---------
    None
    '''
    Base = declarative_base()

    class Category(Base):
        """CATEGORY"""
        __tablename__ = "DIM_CATEGORY"
        __table_args__ = {"schema":"WH"}

        PK = Column(Integer, primary_key=True, autoincrement="auto")
        CATEGORY_CODE = Column(String(350))
        CATEGORY_NAME = Column(String(350))
        CATEGORY_COLOR = Column(String(350))
        LOADED_DATE = Column(DateTime, server_default=func.now())


    class Manufacter(Base):
        """MANUFACTER"""
        __tablename__ = "DIM_MANUFACTER"
        __table_args__ = {"schema":"WH"}

        PK = Column(Integer, primary_key=True, autoincrement="auto")
        MANUFACTER_ID = Column(String(350))
        MANUFACTER_NAME = Column(String(350))
        LOADED_DATE = Column(DateTime, server_default=func.now())


    class Product(Base):
        """PRODUCTS"""
        __tablename__ = 'DIM_PRODUCTS'
        __table_args__ = {"schema":"WH"}

        PK = Column(Integer, primary_key=True, autoincrement="auto")
        SKU = Column(String(350))
        UNITS = Column(Integer)
        TITLE = Column(String(350))
        SUBTITLE = Column(String(350))
        DETAILS = Column(String(350))
        EAN = Column(String(350))
        BRAND = Column(String(350))
        FLAVOR = Column(String(350))
        VARIANT = Column(String(350))
        CATEGORY_CODE = Column(String(350))
        PRODUCT_TYPE = Column(String(350))
        LOADED_DATE = Column(DateTime, server_default=func.now())


    class Sale(Base):
        """SALES"""
        __tablename__ = 'FCT_SALES'
        __table_args__ = {"schema":"WH"}

        PK = Column(Integer, primary_key=True, autoincrement="auto")
        FK_PRODUCT = Column(Integer)
        FK_MANUFACTER = Column(Integer)
        FK_CATEGORY = Column(Integer)
        DELIVERY_ID = Column(String(350))
        AMOUNT = Column(Float)
        CURRENCY = Column(String(350))
        QUANTITY = Column(Integer)
        RETAIL_AMOUNT = Column(Float)
        CREATE_DATE = Column(DateTime)
        UPDATE_DATE = Column(DateTime)
        LOADED_DATE = Column(DateTime, server_default=func.now())

    Base.metadata.create_all(engine_db)