# Integración de Filebeat y Elasticsearch en Docker

Autor: Imanol Anda Garcia

Este proyecto demuestra la configuración y uso de Filebeat para enviar logs a Elasticsearch dentro de un entorno Docker. Se utiliza Filebeat para monitorear y analizar logs generados por un script de Python.

## Explicación de los pasos seguidos

Se siguieron los siguientes pasos para configurar y ejecutar el entorno con Docker Compose:

1. Se creó un `docker-compose.yml` que define dos servicios: `elasticsearch` y `filebeat`.
2. Se configuró Elasticsearch como un nodo único para evitar la complejidad de un clúster.
3. Se preparó una configuración de Filebeat (`filebeat.yml`) para recoger logs de un directorio específico y enviarlos a Elasticsearch.
4. Se desarrolló un script en Python para generar datos ficticios de logs en formato JSON, simulando registros de temperatura y presión.

## Instrucciones de uso

Para iniciar los servicios y ejecutar el entorno, sigue estos pasos:

1. Iniciar Docker Compose:
   docker-compose up -d
2. Verificar que los servicios están ejecutándose:
   docker-compose ps
3. Observar los logs de Filebeat en tiempo real:
   docker-compose logs -f filebeat
4. Utilizar Postman para realizar consultas a Elasticsearch y verificar la ingestión de datos.

## Posibles vías de mejora

Las siguientes mejoras podrían aplicarse al proyecto:

1. Configurar volúmenes persistentes para Elasticsearch para evitar la pérdida de datos.
2. Mejorar la seguridad de Elasticsearch con autenticación y cifrado.
3. Optimizar la configuración de Filebeat para gestionar mejor la rotación y el tamaño de los logs.

## Problemas / Retos encontrados

A lo largo del desarrollo del proyecto, me encontré con varios retos que requirieron soluciones específicas:

- **Conexión Rechazada**: Inicialmente, Filebeat no lograba conectarse con Elasticsearch, lo cual se identificó como un problema de red dentro de Docker. Para resolverlo, me aseguré de que ambos servicios estuvieran configurados en la misma red de Docker y agregué una política de reintentos en Filebeat para manejar los tiempos de inicio de Elasticsearch.

- **Permisos de Archivos**: Al trabajar con volúmenes en Docker, enfrenté problemas de permisos al intentar que Filebeat leyera la configuración y los logs. Este inconveniente se solucionó ajustando los permisos de los archivos en el sistema host para que fueran accesibles al usuario dentro del contenedor de Filebeat.

- **Cambio de Índice en ILM**: Dado que el proyecto requería la implementación de Index Lifecycle Management (ILM) de Elasticsearch, tuve que configurar Filebeat para que pudiera cambiar de índice según las políticas establecidas. Esto implicó reducir las restricciones y configurar adecuadamente `filebeat.yml`.

## Conclusión
La integración de Filebeat y Elasticsearch en Docker ofrece una solución robusta y escalable para el monitoreo de logs. A pesar de los desafíos iniciales, el sistema final funciona eficazmente para recopilar, analizar y visualizar datos de logs.