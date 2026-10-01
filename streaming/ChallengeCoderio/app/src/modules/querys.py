#!/usr/bin/env python
# -*- coding: utf-8 -*-

def exect_querys(engine):
    '''
    run querys inserts in tablas WH

    Parameters
    ----------
    engine : sqlalchemy engine
        engine db
    
    Returns
    ---------
    None
    '''

    category = """
        ALTER SEQUENCE "WH"."DIM_CATEGORY_PK_seq" RESTART;
        TRUNCATE TABLE "WH"."DIM_CATEGORY";
        INSERT INTO "WH"."DIM_CATEGORY" ("CATEGORY_CODE", "CATEGORY_NAME", "CATEGORY_COLOR")
        SELECT DISTINCT category_code, category_name, category_color
        FROM "DLKCUR"."DIM_CATEGORY_INIT";
        """
    index_category = """ CREATE INDEX index_pk ON "WH"."DIM_CATEGORY" ("PK") """


    manufacter = """
        ALTER SEQUENCE "WH"."DIM_MANUFACTER_PK_seq" RESTART;
        TRUNCATE TABLE "WH"."DIM_MANUFACTER";
        INSERT INTO "WH"."DIM_MANUFACTER" ("MANUFACTER_ID", "MANUFACTER_NAME")
        SELECT DISTINCT manufacturer_id, manufacturer_name
        FROM "DLKCUR"."DIM_MANUFACTER_INIT"
        """
    index_manufacter = """ CREATE INDEX index_pk ON "WH"."DIM_MANUFACTER" ("PK") """


    product = """
        ALTER SEQUENCE "WH"."DIM_PRODUCTS_PK_seq" RESTART;
        TRUNCATE TABLE "WH"."DIM_PRODUCTS";
        INSERT INTO "WH"."DIM_PRODUCTS"
        ("SKU", "UNITS", "TITLE", "SUBTITLE", "DETAILS", "EAN", "BRAND", "FLAVOR", "VARIANT", "CATEGORY_CODE", "PRODUCT_TYPE")
        SELECT DISTINCT sku, units, title, subtitle, details, ean, brand, flavor, variant, category_code, product_type
        FROM "DLKCUR"."DIM_PRODUCT_INIT"
        """
    index_product = """ CREATE INDEX index_pk ON "WH"."DIM_PRODUCTS" ("PK") """


    sales_drop = """ DROP TABLE "DLKCUR"."CUR_FCT_SALES" """

    sales = """
        INSERT INTO "WH"."FCT_SALES"(
            "FK_PRODUCT", "FK_MANUFACTER", "FK_CATEGORY"
            , "DELIVERY_ID", "AMOUNT", "CURRENCY", "QUANTITY", "RETAIL_AMOUNT"
            , "CREATE_DATE", "UPDATE_DATE")
            
        SELECT
        table2."PK" AS "FK_PRODUCT"
        , table3."PK" AS "PK_MANUFACTER"
        , table4."PK" AS "PK_CATEGORY"
        , delivery_id, amount, currency, quantity , retail_amount
        , created_date, updated_date
        FROM "DLKCUR"."FCT_SALES_INIT" AS table1

        LEFT JOIN "WH"."DIM_PRODUCTS" AS table2
        ON table1.sku = table2."SKU"

        LEFT JOIN "WH"."DIM_MANUFACTER" AS table3
        ON table1.manufacturer_id = table3."MANUFACTER_ID"

        LEFT JOIN "WH"."DIM_CATEGORY" AS table4
        ON table1.category_code = table4."CATEGORY_CODE"
        """

    querys = [category, index_category, manufacter, index_manufacter, product, index_product, sales_drop, sales]

    conn = engine.connect()
    for query in querys:
        print('Tratando de ejecutar:', query)
        try:
            conn.execute(query)
            print('SUCCESS ... \n')
        except:
            print('ERROR, NO COMPLETADA ... \n')

    conn.close()