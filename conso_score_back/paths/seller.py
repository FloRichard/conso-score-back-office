from flask import Blueprint, request, jsonify, request,render_template, flash, session
from flask_cors import cross_origin
from ..data_access.get_seller_datas import  get_seller_partners_db
from ..data_access.get_datas import get_all_transports_db, get_all_products_db
bpapi = Blueprint('/seller', __name__, url_prefix='/seller')

@bpapi.route("/")
def home():
    return jsonify(get_all_products_db()) #test


@bpapi.route("/<seller_id>/product", methods=['GET','POST'])
def seller_get_product(seller_id):
    #todo parse json request response and fill the var
    bar_code = 123
    maker_product_id = "abc-er"
    price = 2
    quantity = 8
    #call get_product_score(bar_code,maker_product_id, price,quantity)
    return {"conso_score":0, "tax":0} #todo

@bpapi.route("/<seller_id>/makers", methods=['GET'])
def seller_partners(seller_id):
    partners = get_seller_partners_db(seller_id)
    return jsonify(partners)

