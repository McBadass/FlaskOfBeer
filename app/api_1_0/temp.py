from flask import jsonify
import os
import glob
import time
from . import api

# os.system('modprobe w1-gpio')
# os.system('modprobe w1-therm')

test_temps = [("20151", 78.4),
              ("20152", 79.1),
              ("20153", 80.40),
              ("20154", 82.15),
              ("20155", 75.10),
              ("20156", 72.01),
              ("20157", 78.9),
              ("20158", 72.1),
              ("20159", 71.67),
              ("20160", 81.67)]

temps2 = [{'timestamp': '20151', 'temp': 78.4},
          {'timestamp': '20152', 'temp': 81.24},
          {'timestamp': '20153', 'temp': 82.55},
          {'timestamp': '20154', 'temp': 81.24},
          {'timestamp': '20155', 'temp': 87.21},
          {'timestamp': '20156', 'temp': 80.12},
          {'timestamp': '20157', 'temp': 78.83},
          {'timestamp': '20158', 'temp': 83.23},
          {'timestamp': '20159', 'temp': 86.59},
          {'timestamp': '20160', 'temp': 80.32},
          {'timestamp': '20161', 'temp': 90.15},
          ]


base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'


def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines


# Reads temp and returns Fahrenheit temperature
def read_temp_c():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return round(temp_c, 2)


def read_temp_f():
    temp_f = read_temp_c() * 9.0 / 5.0 + 32.0
    return round(temp_f, 2)


@api.route('/temp/', methods=['GET'])
def get_temp():
    return jsonify({'temp_f': read_temp_f()})


@api.route('/temp/<int:numtemps>')
def get_multi_temps(numtemps):
    if numtemps < len(test_temps):
        return jsonify(results=temps2[-numtemps:], encoding='utf-8')
    return jsonify(results=temps2[-len(temps2):], encoding='utf-8')
