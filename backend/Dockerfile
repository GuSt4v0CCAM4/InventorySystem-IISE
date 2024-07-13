# Usar una imagen base de Python
FROM python:3.9

# Instalar las dependencias del sistema necesarias para Tkinter
RUN apt-get update && apt-get install -y python3-tk

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el archivo de requisitos y el código fuente
COPY requirements.txt requirements.txt
COPY . .

# Instalar las dependencias de Python
RUN pip install -r requirements.txt

# Establecer la variable DISPLAY
ENV DISPLAY=$DISPLAY
ENV XAUTHORITY=/tmp/.Xauthority

# Exponer el puerto en el que correrá la aplicación
EXPOSE 5000

# Comando para correr la aplicación
CMD ["python", "app.py"]
