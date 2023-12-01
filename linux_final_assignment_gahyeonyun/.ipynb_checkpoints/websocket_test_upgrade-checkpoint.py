from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import pymysql
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import DataFrame
from random import randrange

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
# Configure MySQL connection
host='localhost'
user='gahyeon'
password='gh'
database='temp'

def get_sensor_data():
    conn = pymysql.connect(host=host, user=user, password=password,
    database=database)
    query = "SELECT max_temp, avg_temp, min_temp, rain_per, wind_per, timestamp FROM ( SELECT * FROM SensorData ORDER BY id DESC LIMIT 100)Var1 ORDER BY id ASC"
    df = pd.read_sql(query, conn)
    df = df.set_index('timestamp')
    conn.close()
    #print(df)
    return df

def generate_plot(df):
    return df.plot(use_index=True, y=["max_temp", "avg_temp", "min_temp", "rain_per", "wind_per"],

kind="line", figsize=(10, 5)).legend(loc='upper left')
@socketio.on('connect')
def handle_connect():
    print('Client connected')
    emit('update_plot', 'Connected') # Send a message to the client on connect

@app.route('/')
def index():
    return render_template('index_plot.html')

@socketio.on('get_plot')
def handle_get_plot():
    sensor_data = get_sensor_data()
    plot = generate_plot(sensor_data)
    plt.savefig('static/plot2.png') # Save the plot as an image
    plt.close() # Close the plot
    emit('update_plot', 'plot2.png') # Send the updated plot filename to the client

if __name__ == '__main__':
    socketio.run(app, port=5001)

