from flask import Flask, render_template
from config import config
from flask_bootstrap import Bootstrap

def create_app(config_name):
  app = Flask(__name__)
  bootstrap = Bootstrap(app)
  app.config.from_object(config[config_name])
  config[config_name].init_app(app)

  # Blueprint is stored in the __init__ file of the 'main' package. Information on Blueprints in README
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)
  
  return app