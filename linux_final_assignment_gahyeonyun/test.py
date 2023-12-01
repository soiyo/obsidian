import datetime
import random
import time
import paho.mqtt.client as mqtt
import pymysql

def on_message(client, userdata, message):
    try:
        global mmmmmhh
        payload = message.payload.decode()
        data = eval(payload)

        db_connection = pymysql.connect(host=db_host,user=db_user,password=db_password,database=db_name)
        cursor = db_connection.cursor()

        print(f'whats this? {data}')
        str_datetime = data['timestamp']
        timestamp = datetime.datetime.strptime(str_datetime, '%Y-%m-%d %H:%M:%S')

        # timestamp = datetime.datetime.strptime(data['time'], '%Y-%m-%d %H:%M:%S')
        # timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        sensordata_id = data['sensordata_id']
        max_temp = data['max_temp']
        avg_temp = data['avg_temp']
        min_temp = data['min_temp']
        rain_per = data['rain_per']
        wind_per = data['wind_per']
        weather = data['weather']

        query = f"INSERT INTO {table_name} (sensordata_id, max_temp, avg_temp, min_temp, rain_per, wind_per, timestamp, weather) VALUES  (%s,%s,%s,%s,%s,%s, %s, %s)"
        cursor.execute(query, (sensordata_id, max_temp, avg_temp, min_temp, rain_per, wind_per, timestamp, weather))

        db_connection.commit()
        db_connection.close()
        print(f"Received and stored: Time: {timestamp}, SID: {sensordata_id}, MAX_TEMP:{max_temp}, AVG_TEMP:{avg_temp},MIN_TEMP:{min_temp},RAIN: {rain_per}%, WIND: {wind_per}%, weather: {weather}")
    except Exception as e:
        # print(datetime.datetime.now())
        print(f"Error: {e}")

def simulate_and_send(client):
    while True:
        current_time = datetime.datetime.now()
        
        sensordata_id = random.randint(1,4)
        max_temp = random.uniform(20, 30)
        min_temp = random.uniform(-10, 19)
        tot_temp = max_temp+min_temp
        avg_temp = (tot_temp)/2

        
        rain_per = random.uniform(0, 100)
        wind_per = random.uniform(0, 100)
        
        if (max_temp >= 20) & (min_temp >=10) : #20 ~ 10
            weather = 'sunny'
            if rain_per >= 50:
                weather = 'sunny and rainy'
            elif wind_per >= 50:
                weather = 'sunny and windy'
        elif (max_temp <= 19) & (min_temp <=0) : #19 ~ 0
            weather = 'cold'
            if rain_per >= 50:
                weather = 'cold and rainy'
            elif wind_per >= 50:
                weather = 'cold and windy'
        else :
            weather = 'not sunny or cold'
            if rain_per >= 50:
                weather = 'not sunny or cold and rainy'
            elif wind_per >= 50:
                weather = 'not sunny or cold and windy'

        data = {  
                'sensordata_id': sensordata_id,
                'max_temp': max_temp,
                'avg_temp': avg_temp,
                'min_temp': min_temp,
                'rain_per': rain_per,
                'wind_per': wind_per,
                'timestamp': current_time.strftime('%Y-%m-%d %H:%M:%S'), 
                'weather':weather
                }
        client.publish(topic, str(data)) # Publish data to MQTT broker
        print(f"Time: {current_time}, SID: {sensordata_id}, MAX_TEMP:{max_temp}, AVG_TEMP:{avg_temp:.2f},MIN_TEMP:{min_temp},RAIN: {rain_per}%, WIND: {wind_per}%, weather: {weather}")
        time.sleep(1)

broker_address = 'broker.hivemq.com'
broker_port = 1883
topic = 'sensors'

db_host = 'localhost'
db_user = 'gahyeon'
db_password = 'gh'
db_name = 'temp'
table_name = 'SensorData'

mqtt_client = mqtt.Client()
mqtt_client.connect(broker_address, broker_port)

mqtt_client.subscribe(topic)
mqtt_client.on_message = on_message
mqtt_client.loop_start()

simulate_and_send(mqtt_client)