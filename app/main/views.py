from . import main
from .forms import GenerateKingdomForm
from flask import make_response, render_template, request
from dominion.kingdom import Kingdom

@main.route('/', methods=['GET', 'POST'])
def index(requireActions : bool = None):
  kingdom = Kingdom()
  form = GenerateKingdomForm()
  if form.validate_on_submit():
    kingdom.included_expansions = [request.form['expansions']]
    kingdom.generate()
  return render_template('index.html', kingdom=kingdom, form=form)
