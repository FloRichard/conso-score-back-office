from flask import Blueprint,jsonify
from ..data_access.get_datas import get_all_transports_db,get_product_by_barcode
bpapi = Blueprint('/datas', __name__, url_prefix='/datas')

@bpapi.route("/transport")
def get_transportation_list():
    transports = get_all_transports_db()
    return jsonify(transports)

@bpapi.route("/product/<bar_code>")
def get_product_with_bar_code(bar_code):
    product = get_product_by_barcode(bar_code)
    return jsonify(product)