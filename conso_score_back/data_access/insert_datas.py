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
                        (maker_id, product_id) values (%s,%s)",(maker_id, product_id))
        get_db().commit()
    except Exception as e:
        print(e)
        return "an error occured while registering the product"
       

