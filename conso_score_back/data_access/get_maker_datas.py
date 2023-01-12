from .db_access import get_db

"""get the products proposed by the maker"""
def get_maker_products_db(maker_id):
    try:
        cursor = get_db().cursor()
        cursor.execute("SELECT *  FROM product \
                        JOIN maker_stock ON maker_stock.product_id = product.product_id\
                        JOIN maker ON maker.maker_id = maker_stock.maker_id\
                        WHERE maker.maker_id=%s;",(maker_id,))
        products = []

        for element in cursor.fetchall():
            products.append({"product_id":element[0], "name":element[1], "price":element[2], "carbon_footprint":element[3],"quantity_unity":element[4],"category_id":element[5],"expedition_transport_id":element[6]})
        return products
    except Exception as e:
        print(e)
        print("an error occured while fetching maker's products")

"""get one product proposed by the maker"""
def get_maker_product_db(maker_id, product_id):
    try:
        cursor = get_db().cursor()
        cursor.execute("SELECT * FROM product\
                        JOIN maker_stock ON maker_stock.product_id = product.product_id\
                        JOIN maker ON maker.maker_id = maker_stock.maker_id\
                        WHERE maker.maker_id=%s \
                        AND product.product_id=%s;",(maker_id,product_id))
        result = cursor.fetchone()
        return {"id":result[0], "name":result[1], "price":result[2], "carbon_footprint":result[3], "quantity_unity":result[4], "category_id":result[5], "expedition_transport_id":result[6]}
    except Exception as e:
        print(e)
        return "an error occured while fetching maker's product"