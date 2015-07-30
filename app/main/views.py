from flask import render_template, url_for, current_app, session, redirect
from .. import db
from ..models import TempSensor, SensorData
from . import main
from .forms import SensorCreate


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
