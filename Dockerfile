# Usa una imagen ligera de Python 3.8
FROM python:3.8-slim-buster

# Establece un directorio de trabajo
WORKDIR /app

# Copia los requerimientos e instala las dependencias
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copia el código de la aplicación al contenedor
COPY src/ .

# Ejecuta la aplicación con Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
