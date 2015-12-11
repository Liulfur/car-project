from flask_wtf import Form 
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

class AddCarForm(Form):
	car_id = IntegerField()
	make = StringField('Make', validators=[DataRequired()])
	model = StringField('Model', validators=[DataRequired()])
	color = StringField('Color', validators=[DataRequired()])
	year = IntegerField('Year', validators=[DataRequired()])
	odom = IntegerField('Odometer', validators=[DataRequired])
	oil = StringField('Oil', validators=[DataRequired()])
	trans = StringField('Transmission', validators=[DataRequired])
	brake = StringField('Brake', validators=[DataRequired])
