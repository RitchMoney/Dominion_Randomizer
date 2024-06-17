from wtforms import SubmitField, RadioField
from flask_wtf import FlaskForm

from dominion_data.util import get_loaded_expansion_names 

class GenerateKingdomForm(FlaskForm):
  expansions = RadioField('Sets', choices=get_loaded_expansion_names())
  submit = SubmitField('Generate')