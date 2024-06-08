from . import main
from flask import make_response, render_template
from dominion.dominion import Kingdom, Card

@main.route('/', methods=['GET'])
def index(requireActions : bool = None):
  kingdom = Kingdom()
  response = make_response('<h1>Hello Dominion!</h1>')
  return render_template('index.html', kingdom=kingdom)