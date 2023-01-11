from flask import Blueprint, request, jsonify, request,render_template, flash, session
from flask_cors import cross_origin

bpapi = Blueprint('/seller', __name__, url_prefix='/seller')

@bpapi.route("/")
def home():
    return "seller"


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
    #todo call get_seller_partners
    return jsonify([{"id":"abc-ze", "name":"la ferme ficelle", "location":"caen"}, {"id":"abc-azeuaz", "name":"la ferme de bretagne", "location":"rennes"}])