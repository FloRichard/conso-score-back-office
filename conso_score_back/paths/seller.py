from flask import Blueprint, request, jsonify, request,render_template, flash, session
from flask_cors import cross_origin
from ..data_access.get_seller_datas import  get_seller_partners_db
from ..data_access.get_datas import get_all_transports_db, get_all_products_db
from ..data_access.insert_datas import register_seller_product_db
bpapi = Blueprint('/seller', __name__, url_prefix='/seller')

@bpapi.route("/")
def home():
    return jsonify(get_all_products_db()) #test


@bpapi.route("/<seller_id>/product", methods=['GET','POST'])
def seller_get_product(seller_id):
    if request.method == 'GET':
        #todo parse json request response and fill the var
        seller_id = '5a39c805-4e15-4944-80af-333d2d11bced'
        product_id = '87a1e36f-c193-4640-ba98-fd8dd58e25ce'
        price = 8
        bar_code = 456
        quantity = 5
        return register_seller_product_db(seller_id, product_id, price, bar_code,quantity)
        
    elif request.method == 'POST':
        #todo parse json request response and fill the var

        #call get_product_score(bar_code,maker_product_id, price,quantity)
        return {"conso_score":0, "tax":0}

@bpapi.route("/<seller_id>/makers", methods=['GET'])
def seller_partners(seller_id):
    partners = get_seller_partners_db(seller_id)
    return jsonify(partners)

