# API para consultar la Unidad de Fomento en Python Flask

API en Python que permite a los usuarios consultar el valor de la Unidad de Fomento para una fecha específica.

Esta API se creó usando Python con su framework Flask y con Pipenv.

## Instalación e intrucciones de ejecución
⚠️ Asegurarse de tener instalado `python 3.6+` y corriendo en su computadora

Instale los requisitos en un virtualenv o en el entorno de su elección

```sh
pip install pipenv
pipenv shell
pipenv install
```

### Ejecución del proyecto
```sh
pipenv run server
```

## Endpoints

```txt
GET /api/v1/indicator/<string:date>
```

### GET /api/v1/indicator/<string:date>

Este endpoint devuelve (/api/v1/indicator/05-05-2023):

```javascript
{
    "valor": 35903.96
}
```

## Test
Para ejecutar los test debemos primero tener corriendo el proyecto en una terminal `pipenv run server`.

Y luego en otra terminal ejecutar los siguientes comandos: 

```sh
pipenv shell
pipenv run test
```