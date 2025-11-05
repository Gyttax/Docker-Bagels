
# Dockerfile para el juego Bagels
# Imagen oficial de Python

FROM python:3.12-slim

# Establecer directorio del 

WORKDIR /home/sara/Programación/"Hola Python"/juego

COPY requirements.txt .
COPY game.py .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Comando de entrada del contenedor para ejecutar el juego

CMD [ "python", "game.py" ]

