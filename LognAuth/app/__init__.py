import os
from flask import Flask

def create_app(test_config=None):
	app = Flask(__name__,instance_relative_config=True)
	app.config.from_mapping(
		SECRET_KEY='dev',
		DATABASE=os.path.join(app.instance_path,'login.sqlite'),
	)

	if test_config is None:
		app.config.from_pyfile('config.py',silent=True)
	else:
		app.config.from_mapping(test_config)

	#ensure that instance folder exists
	try:
		os.makedirs(app.instance_path)
	except OSError:
		pass

	#test Route
	@app.route('/heartbeat')
	def heartbeat():
		return {'status' : 200, 'message':'Alive!'}
	from . import db
	db.init_app(app)
	from . import auth
	app.register_blueprint(auth.bp)

	return app
