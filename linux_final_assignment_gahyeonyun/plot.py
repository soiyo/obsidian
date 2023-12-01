import datetime
import random
import matplotlib.pyplot as plt
# Simulation parameterss 
start_date = datetime.datetime(2023, 1, 1, 0, 0, 0)
end_date = datetime.datetime(2023, 1, 2, 0, 0, 0)
time_delta = datetime.timedelta(minutes=10)
timestamps = [start_date + i*time_delta for i in range(int((end_date - start_date) / time_delta))]

# Simulating temperature, humidity, and illuminance
max_temp = [random.uniform(20, 30) for _ in range(len(timestamps))]
min_temp = [random.uniform(0, 19) for _ in range(len(timestamps))]
tot_temp = max_temp+min_temp
avg_temp = [sum(tot_temp)/len(tot_temp) for _ in range(len(timestamps))] 


rain_per = [random.uniform(0, 100) for _ in range(len(timestamps))]
wind_per = [random.uniform(0, 100) for _ in range(len(timestamps))]

# Plotting the simulation results
plt.figure(figsize=(10, 5))
plt.plot(timestamps, max_temp, label='MAX Temperature (°C)')
plt.plot(timestamps, avg_temp, label='AVG Temperature (°C)')
plt.plot(timestamps, min_temp, label='MIN Temperature (°C)')
plt.plot(timestamps, rain_per, label='Rainy Percent(%)')
plt.plot(timestamps, wind_per, label='Windy Percent(%)')
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Temperature Prediction System')
plt.legend()
plt.grid(True)
plt.show()