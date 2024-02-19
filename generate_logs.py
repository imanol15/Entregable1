import json
import random
import datetime

# Generar datos de sensores con valores de presión y temperatura aleatorios y escribirlos con saltos de línea
def generar_y_escribir_datos_con_saltos_de_linea(file_path="logs/dummy_logs.json"):
    with open(file_path, "w") as file:
        for i in range(100):
            data_entry = {
                "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "temperature": round(random.uniform(20.0, 30.0), 2),  # Temperatura en grados Celsius
                "pressure": round(random.uniform(1.0, 1.5), 2)        # Presión en atmósferas
            }
            # Convertir a JSON y añadir un salto de línea al final
            json_data = json.dumps(data_entry) + "\n"
            # Escribir en el archivo
            file.write(json_data)

# Llamar a la función para generar y escribir los datos con saltos de línea
generar_y_escribir_datos_con_saltos_de_linea("logs/dummy_logs.json")

