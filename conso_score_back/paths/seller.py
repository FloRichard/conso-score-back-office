from flask import Blueprint, request, jsonify, request, render_template, flash, session
from flask_cors import cross_origin
from ..data_access.get_seller_datas import get_seller_partners_db
from ..data_access.get_datas import get_all_transports_db
from ..data_access.insert_datas import register_seller_product_db
bpapi = Blueprint('/seller', __name__, url_prefix='/seller')


@bpapi.route("/<seller_id>/product", methods=['POST', 'OPTIONS'])
@cross_origin(headers=['Content-Type'])
def seller_get_product(seller_id):
    if request.method == 'POST':
        datas = request.json
        product_id = datas["product_id"]
        price = datas["price"]
        bar_code = datas["bar_code"]
        quantity = datas["quantity"]
        return register_seller_product_db(seller_id, product_id, price, bar_code, quantity)
    return ""


@bpapi.route("/<seller_id>/makers", methods=['GET'])
@cross_origin()
def seller_partners(seller_id):
    partners = get_seller_partners_db(seller_id)
    return jsonify(partners)
