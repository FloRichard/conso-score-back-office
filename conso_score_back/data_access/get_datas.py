from .db_access import get_db
import random
   
def get_product_score():
    #insertion du produit dans le stock du vendeur => Un stock par vendeur
    #si pas de stock il faut le créer
    #calcul du score
    return ""

def get_all_transports_db():
    cursor = get_db().cursor()
    cursor.execute("SELECT expedition_transport_id, name FROM expedition_transport")
    transports = []
    for element in cursor.fetchall():
        transports.append({"transport_id":element[0], "name":element[1]})
    return transports

def get_product_by_barcode(bar_code):
    try:
        cursor = get_db().cursor()
        cursor.execute("SELECT * FROM seller_product WHERE seller_product.bar_code=%s",(bar_code,))
        result = cursor.fetchone()
        product = {"product_id":result[1],"price":result[2],"conso_score":result[3], "bar_code":result[4], "tax":result[5]}
        cursor.execute("SELECT * FROM product WHERE product_id = %s", (product['product_id'],))
        result = cursor.fetchone()
        product["name"] = result[1]
        product["carbon_foot_print"] = result[3]
        product["quantity_unity"] = result[4]
        category = result[5]
        transport_cat = result[6]
        print("product", product)
        cursor.execute("SELECT name FROM category WHERE category_id = %s", (category,))
        product["category"] = cursor.fetchone()[0]

        cursor.execute("SELECT name FROM expedition_transport WHERE expedition_transport_id = %s", (transport_cat,))
        product["transport"] = cursor.fetchone()[0]
        print(product)
        return product
    except Exception as e:
        print(e)
        return "an error occured while fetching product by barcode"
        
def get_transport_by_id_db(transport_id):
    cursor = get_db().cursor()
    cursor.execute("SELECT name, kilometer_carbon_footprint FROM expedition_transport WHERE expedition_transport_id = %s", (transport_id,))
    result = cursor.fetchone()
    transport = {"name":result[0], "carbon_footprint":result[1]}
    return transport

def get_category_by_id_db(category_id):
    cursor = get_db().cursor()
    cursor.execute("SELECT name FROM category WHERE category_id = %s", (category_id,))
    result = cursor.fetchone()
    category = {"name":result[0]}
    return category