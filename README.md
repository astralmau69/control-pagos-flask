# Control de pagos — Pasanaku

Aplicación web para llevar el control de aportes mensuales de un pasanaku: quién pagó, cuánto, y el comprobante en foto.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)

---

## El problema

Un pasanaku se administra normalmente en un cuaderno o un grupo de WhatsApp. Los dos fallan igual: alguien dice que ya pagó, nadie encuentra el comprobante, y la discusión queda sin resolver.

Esta app guarda el monto **y la foto del comprobante** por persona y por mes, así que el respaldo siempre está.

---

## Qué hace

- Vista por mes — se elige el mes y se ve el estado de aportes de todos los participantes
- Registro de monto por persona
- Carga de comprobante en foto, asociado a esa persona y ese mes
- Persistencia en SQLite, sin necesidad de servidor de base de datos

---

## Stack

`Python` · `Flask` · `SQLite` · `Jinja2`

---

## Estructura

```
├── app.py           # rutas y lógica de la aplicación
├── init_db.py       # creación e inicialización del esquema
├── requirements.txt
├── templates/       # vistas Jinja2
└── static/
    └── uploads/     # comprobantes cargados
```

---

## Nota de implementación

El esquema guarda un par de columnas por mes (`enero`, `enero_foto`, `febrero`, …), lo que obliga a construir el nombre de columna dinámicamente en la consulta. Para que eso no abra una inyección SQL, el mes recibido por query string se valida contra una lista blanca antes de tocar la consulta:

```python
MESES = ['enero', 'febrero', ..., 'diciembre']

mes_actual = request.args.get('mes', 'enero').lower()
if mes_actual not in MESES:
    mes_actual = 'enero'
```

Cualquier valor fuera de los doce meses cae al valor por defecto y nunca llega a la base de datos.

---

## Correr el proyecto

```bash
pip install -r requirements.txt
python init_db.py     # crea database.db
python app.py         # http://localhost:5000
```

La carpeta `static/uploads/` se crea sola al arrancar.

---

**Autor** — [Mauricio Aparicio](https://github.com/astralmau69) · apariciomau3@gmail.com
