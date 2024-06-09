from wtforms import SubmitField
from flask_wtf import FlaskForm 

class GenerateKingdomForm(FlaskForm):
  submit = SubmitField('Generate')