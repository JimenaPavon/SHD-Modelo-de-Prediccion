//SHP-Jimena Pavon Guzman

# Servicio de Predicción
 Este es un servicio REST API que simula el uso de un modelo de predicción y está configurado para ejecutarse mediante contenedores Docker.
 El servicio proporciona un endpoint que realiza una operación básica de suma para simular una predicción.
 
 ## Información del Servicio- 
 **Lenguaje**: Python- 
 **Framework**: Flask- 
 **Contenedorización**: Docker
 
 ## Requerimientos
 Para ejecutar este proyecto, necesitas tener instalados los siguientes programas:
 - Python 3.x
 - Docker
 - - Git
   - 
 ## Instalación
 Sigue estos pasos para instalar y ejecutar el proyecto:
 1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/tu-usuario/prediction_service.git
   cd prediction_service/app
   ```
 2. **Construir la imagen Docker:**
   ```bash
   docker build -t prediction_service .
   ```
 3. **Ejecutar el contenedor Docker:**
   ```bash
   docker run -d -p 5000:5000 prediction_service
   ```
 ## Uso (Producción)
 ### Endpoints
 #### Página de bienvenida
 - **URL:** `/`
 - **Método:** GET
- **Descripción:** Muestra una página de bienvenida.
- 
**Ejemplo de solicitud:**
 ```bash
 curl http://localhost:5000/
 ```
 **Respuesta:**
 ```
 Bienvenido al Servicio de Predicción
 ```
 #### Predicción (Simulación)
 - **URL:** `/predict`
 - **Método:** POST
 - **Descripción:** Realiza una operación de suma con dos números proporcionados en el cuerpo de la solicitud.
 - 
 **Ejemplo de solicitud:**
 ```bash
 curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d '{"num1": 5, "num2": 3}'
 ```
 **Respuesta:**
```json
 {
 }
  "prediction": 8
 ```
 ## Uso (Desarrollo)
 ### Requerimientos de Desarrollo- **Instalar dependencias:**
  ```bash
  pip install -r requirements.txt
  ```
 ### Ejecución en Entorno de Desarrollo
 Para ejecutar el servicio en un entorno de desarrollo, sigue estos pasos:
 1. **Iniciar el servidor Flask:**
   Navega al directorio del proyecto y ejecuta:
   ```bash
   cd app
   python app.py
   ```
 2. **Acceder al servicio:**
   El servicio estará disponible en `http://localhost:5000`.
