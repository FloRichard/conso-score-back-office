from .db_access import *

def register_maker_product_db(maker_id,name, price, carbon_foot_print, quantity_unity, category_id, expedition_transport_id):
    try:
        cursor = get_db().cursor()
        cursor.execute("insert into public.product \
                        (name, price, carbon_footprint,\
                         quantity_unity, category_id, expedition_transport_id) \
                        values (%s,%s,%s,%s,%s, %s) RETURNING product_id",(name, price, carbon_foot_print, quantity_unity, category_id, expedition_transport_id))
        product_id = cursor.fetchone()

        cursor.execute("insert into public.maker_stock \
                        (maker_id, product_id) values (%s,%s)",(maker_id, product_id[0]))
        get_db().commit()
    except Exception as e:
        print(e)
        return "an error occured while registering the product"
       
def register_seller_product_db(seller_id, product_id, price, bar_code,quantity):
    try: 
        cursor = get_db().cursor()
        #fetch seller_stock_id
        cursor.execute("SELECT DISTINCT seller_stock_id FROM seller_stock\
                        JOIN seller ON seller.seller_id=seller_stock.seller_id\
                        WHERE seller.seller_id=%s",(seller_id,))
        seller_stock_id = cursor.fetchone()

        conso_score, tax = calculate_conso_score(product_id, quantity)
        if tax == -1:
            return  {"conso_score":-1, "tax":-1}#an error occured 

        #insert seller_product
        cursor.execute("insert into public.seller_product\
            ( product_id, price, conso_score, bar_code, tax)\
            values (%s,%s, %s,%s, %s) RETURNING seller_product_id",(product_id, price, conso_score, bar_code, tax))
        seller_product_id = cursor.fetchone()

        if seller_stock_id == None:
            cursor.execute("insert into public.seller_stock\
                (seller_product_id, seller_id, quantity)\
                values (%s,%s, %s)",(seller_product_id[0], seller_id, quantity))
        else:
            cursor.execute("insert into public.seller_stock\
                (seller_stock_id, seller_product_id, seller_id, quantity)\
                values (%s, %s,%s, %s)",(seller_stock_id[0], seller_product_id[0], seller_id, quantity))

            get_db().commit()
            return {"conso_score":conso_score, "tax":tax}
    except Exception as e:
        print(e)
        return "an error occured while registering the seller product"

def calculate_conso_score(product_id, quantity):
    try : 
        cursor = get_db().cursor()
        cursor.execute("SELECT carbon_footprint FROM product WHERE product_id=%s",(product_id,))
        carbon_footprint = cursor.fetchone()[0]
        conso_score = int(carbon_footprint) * int(quantity) / 100 #TOTO ADAPTER
        taxe = int(conso_score) * 0.05
        return int(conso_score), int(taxe)
    except Exception as e:
        print(e)
        return "an error occured while calculating the conso score", -1
