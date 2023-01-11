from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
from ..data_access.get_maker_datas import get_maker_products_db,get_maker_product_db
from ..data_access.insert_datas import register_maker_product_db
bpapi = Blueprint('/maker', __name__, url_prefix='/maker')


@bpapi.route("/")
def home():
    return "maker"

@bpapi.route("/<maker_id>/product", methods=['POST'])
def register_maker_product(maker_id):
    if request.method == "POST":
        #todo parse post result
        datas = request.form
        name = datas["name"]
        price = datas["price"]
        carbon_footprint = datas["carbon_footprint"]
        quantity_unity = datas["quantity_unity"]
        category_id = datas["category_id"]
        expedition_transport_id = datas["expedition_transport_id"]
        register_maker_product_db(maker_id,name, price, carbon_footprint, quantity_unity, category_id, expedition_transport_id)
        return "success" #200OK

@bpapi.route("/<maker_id>/products", methods=['GET'])
def get_maker_products(maker_id):
    products = get_maker_products_db(maker_id)
    return jsonify(products)

@bpapi.route("/<maker_id>/product/<product_id>", methods=['GET'])
def get_maker_product(maker_id, product_id):
    product = get_maker_product_db(maker_id, product_id)
    return jsonify(product) #one product information

