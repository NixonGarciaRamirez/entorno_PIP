#aqui vamos a decir concual version de pyhon va a iniciar
FROM python:3.10

#ahora creamos una carpeta dentro del contenedor
WORKDIR /app
#ahora vamos a copiar el archivo de las depensencias
#a la izquierda esta el archivo original y a la derecha esta a donde lo queremos mandar
COPY requirements.txt /app/requirements.txt

#ahora vamos a instalar las dependencias o los modulos, ademas de eso pdemos decirle que no
#ajecute el cache y que se hay alguna actualizacion del pip lo haga
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

#por ultimo decimos que copee todos los codigo y que los mande a la carpeta app
COPY . /app/

#ahora generamos este comando para que nuestro contenedor se ejecute de forma inficnata
#si nos percatamos se genero un ciclo while infinito con el lenguaje bash
CMD bash -c "while true; do sleep 1; done"