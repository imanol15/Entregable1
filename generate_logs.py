
import json
import random
import datetime

# Generar datos de sensores con valores de presión y temperatura aleatorios
sensor_data = []
for i in range(100):
    data_entry = {
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "temperature": round(random.uniform(20.0, 30.0), 2),  # Temperatura en grados Celsius
        "pressure": round(random.uniform(1.0, 1.5), 2)        # Presión en atmósferas
    }
    sensor_data.append(data_entry)

# Escribir los datos en un archivo JSON en el directorio actual
file_path = "logs/dummy_logs.json"
with open(file_path, "w") as file:
    json.dump(sensor_data, file, indent=4)

