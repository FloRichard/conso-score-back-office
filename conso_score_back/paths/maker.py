from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
from ..data_access.get_maker_datas import get_maker_products_db,get_maker_product_db
from ..data_access.insert_datas import register_maker_product_db
bpapi = Blueprint('/maker', __name__, url_prefix='/maker')


@bpapi.route("/")
def home():
    return "maker"

@bpapi.route("/<maker_id>/product", methods=['POST', 'GET'])
def register_maker_product(maker_id):
    if request.method == "GET": #test
        name= "Pomme"
        price=1.0
        carbon_footprint= 10.0
        quantity_unity="Kg"
        category_id= "9fa21198-325a-4f8b-9800-6cbe84346bb4"
        expedition_transport_id= "00f95a18-4736-484e-9a3d-f23703fb95c8"
        register_maker_product_db(maker_id,name, price, carbon_footprint, quantity_unity, category_id, expedition_transport_id)
        return "success" #200OK
    elif request.method == "POST":
        #todo parse post result
        register_maker_product_db(name, price, carbon_footprint, quantity_unity, category_id, expedition_transport_id)

@bpapi.route("/<maker_id>/products", methods=['GET'])
def get_maker_products(maker_id):
    products = get_maker_products_db(maker_id)
    return jsonify(products)

@bpapi.route("/<maker_id>/product/<product_id>", methods=['GET'])
def get_maker_product(maker_id, product_id):
    product = get_maker_product_db(maker_id, product_id)
    return jsonify(product) #one product information

