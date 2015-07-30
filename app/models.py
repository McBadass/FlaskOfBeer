from . import db


class TempSensor(db.Model):
    __tablename__ = 'temp_sensors'
    id = db.Column(db.Integer, primary_key=True)
    serial = db.Column(db.String(64), unique=True)
    sensor_model = db.Column(db.String(64), unique=False)
    sensor_name = db.Column(db.String(64), unique=True)
    sensor_location = db.Column(db.String(64), unique=False)
    scan_frequency = db.Column(db.Integer, unique=False)
    sensor_data = db.relationship('SensorData', backref='TempSensor', lazy='dynamic')

    def __init__(self, sensor_name):
        self.sensor_name = sensor_name

    def __repr__(self):
        return '<Temp Sensor %r>' % self.sensor_name


class SensorData(db.Model):
    __tablename__= 'sensor_data'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime)
    temp_sensor_id = db.Column(db.Integer, db.ForeignKey('temp_sensors.id'))
    value = db.Column(db.Float)
