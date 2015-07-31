from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SensorCreate(Form):
    sensor_name = StringField('What is the name of the sensor?', validators=[DataRequired()])
    serial = StringField('What is the serial number of this sensor?', validators=[DataRequired()])
    submit = SubmitField('Save Me!')
