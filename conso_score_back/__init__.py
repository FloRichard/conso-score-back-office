from flask import Flask
from flask import g

def create_app(debug=False):
	app = Flask(__name__)
	app.debug = debug

	from .paths import seller
	app.register_blueprint(seller.bpapi)

	from .paths import maker
	app.register_blueprint(maker.bpapi)

	from .paths import datas 
	app.register_blueprint(datas.bpapi)
	return app