from flask import Blueprint,jsonify
from ..data_access.get_datas import get_all_transports_db,get_product_by_barcode
from flask_cors import cross_origin

bpapi = Blueprint('/datas', __name__, url_prefix='/datas')

@bpapi.route("/transport", methods=['GET'])
@cross_origin()
def get_transportation_list():
    transports = get_all_transports_db()
    return jsonify(transports)

@bpapi.route("/product/<bar_code>")
@cross_origin()
def get_product_with_bar_code(bar_code):
    product = get_product_by_barcode(bar_code)
    return jsonify(product)