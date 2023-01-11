from flask import Blueprint, request, jsonify, request,render_template, flash, session
from flask_cors import cross_origin
from passlib.hash import sha256_crypt
from ..data_access.get_datas import get_categories_user,pick_card_user, get_random_cards
from ..data_access.insert_datas import insert_card_db, insert_category_db, insert_user_db, check_user_login_unicity

bpapi = Blueprint('/maker', __name__, url_prefix='/maker')


@bpapi.route("/")
def home():
    return "maker"

@bpapi.route("/<maker_id>/product", methods=['POST'])
def register_maker_product(maker_id):
    #todo parse post result
    id= "are_ze"
    name= "string"
    price=0
    carbon_foot_print= 0
    quantity_unity="string"
    category_id= "string"
    expedition_transport_id= "string"
    #todo call resiter_maker_product
    return "" #200OK

@bpapi.route("/<maker_id>/products", methods=['GET'])
def get_maker_products(maker_id):
    #todo call get_maker_products
    return "" #jsonify([list of products])

@bpapi.route("/<maker_id>/product/<product_id>", methods=['GET'])
def get_maker_product(maker_id, product_id):
    #todo call get_product
    return #one product information