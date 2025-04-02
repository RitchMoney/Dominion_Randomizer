from wtforms import widgets, SubmitField, SelectMultipleField
from flask_wtf import FlaskForm 


class MultiCheckboxField(SelectMultipleField): #credit https://gist.github.com/doobeh/4668212
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class GenerateKingdomForm(FlaskForm):
  expansions = MultiCheckboxField('Expansions', choices=[('Intrigue', 'Intrigue'), ('Dark_Ages', 'Dark Ages'), ('Cornucopia', 'Cornucopia')])
  submit = SubmitField('Generate')