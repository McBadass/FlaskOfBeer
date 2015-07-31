from flask import render_template, url_for, flash
from .. import db
from . import sensors
from ..models import TempSensor
from .forms import SensorCreate


@sensors.route('/sensors', methods=['GET', 'POST'])
def addsensor():
    form = SensorCreate()
    return render_template('sensors/addsensor.html', form=form)
