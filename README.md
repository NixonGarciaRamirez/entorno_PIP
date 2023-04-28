# EJERCICIO DE ENTORNOS PIP💚♻
## OBJETIVO
### Obtener fluides en materia de servidores GitHub tomando como base los conocimientos basicos en comandos GIT
## COMO SE REALIZARA
### La idea es tomar subir el juego de piedra papel y tijera a mi cuenta de GitHub, este juego se desarrollo en el curso de fundamentos de Python.

## COMO CORRER EL JUEGO
### SE PUEDE CORRER DENTRO DE CUALQUIER ADITOR DE CODIGO PYTHON, SIN EMBARGO SE PUEDE CORRER DE FORMA AUTOMATICA DENTRO DE WSL CON EL SIGUIENTE COMANDO

`cd game`
`python3 juego.py`





###DIAGRAMA DE FLUJO DEL JUEGO
```flow
st=>start: ESCRIBE 1 PARA COMENZAR
op=>operation: SELECCIONA UN ATRIBUTO DEL JUEGO
cond=>condition: SI EL RESULTADO ES IGUAL AL DEL 
COMPUTADORESTE TENDERA A REPETIR LA 
.PREGUNTA

e=>end: SE AGREGA UN PUNTO 
AL GANADOR

st->op->cond
cond(yes)->e
cond(no)->op
```


