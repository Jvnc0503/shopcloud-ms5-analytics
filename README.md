# MS5 - Analytics Service 

Microservicio de analítica desarrollado con FastAPI para el proyecto ShopCloud. Proporciona endpoints para consultas analíticas sobre datos almacenados en AWS Athena.


### 🚀 Funcionalidades

El servicio expone los siguientes endpoints:

* /
* /analytics/ventas-por-categoria
* /analytics/top-productos
* /analytics/usuarios-activos
* /analytics/ingresos-por-mes

Cada endpoint de analytics ejecuta consultas SQL en Athena y retorna resultados en formato JSON.

⸻

### 🧱 Tecnologías utilizadas

* FastAPI
* Uvicorn
* Docker
* AWS Athena
* AWS S3
* boto3

⸻

### ⚙️ Configuración

El servicio requiere variables de entorno configuradas en un archivo .env:


AWS_ACCESS_KEY_ID=...

AWS_SECRET_ACCESS_KEY=...

AWS_REGION=...

ATHENA_DATABASE=...

ATHENA_OUTPUT=...

⸻

### 🐳 Ejecución con Docker


#### 1. Construir la imagen:

docker build -t ms5-analytics .


#### 2. Ejecutar el contenedor:

docker run -d -p 8005:8005 --env-file .env ms5-analytics

⸻

### 🌐 Acceso

El servicio se encuentra desplegado en una instancia EC2 con Elastic IP:

http://3.83.210.43:8005/docs

⸻

### 📊 Estado del servicio

* ✅ Microservicio desplegado en EC2
* ✅ Endpoints funcionales
* ✅ Integración con Athena configurada mediante credenciales AWS

⸻

### 📄 OpenAPI

El archivo openapi.yml describe los endpoints del servicio y puede utilizarse para integración o documentación adicional.

Los endpoints de analytics retornan un objeto con campos como status, query_id y data, segun el resultado de la consulta.

⸻

### 👥 Notas

* El acceso a Athena depende de credenciales válidas del equipo.
* El servicio puede ejecutarse localmente o en la nube con distinta configuración de credenciales.

