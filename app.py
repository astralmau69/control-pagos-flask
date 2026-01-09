import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import sqlite3

app = Flask(__name__)

# CONFIGURACIÓN DE CARPETA DE IMÁGENES
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# Crear la carpeta si no existe
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

MESES = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 
         'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    mes_actual = request.args.get('mes', 'enero').lower()
    if mes_actual not in MESES: mes_actual = 'enero'

    conn = get_db_connection()
    # Ahora traemos el MONTO y la FOTO del mes seleccionado
    query = f"SELECT id, paterno, nombre, {mes_actual} as monto, {mes_actual}_foto as foto FROM pagos"
    personas = conn.execute(query).fetchall()

    query_total = f"SELECT SUM({mes_actual}) FROM pagos"
    total = conn.execute(query_total).fetchone()[0]
    conn.close()
    
    if total is None: total = 0

    return render_template('index.html', personas=personas, mes_actual=mes_actual, total=total, meses=MESES)

@app.route('/guardar', methods=['POST'])
def guardar():
    id_persona = request.form['id']
    mes = request.form['mes']
    monto = request.form['monto']
    if not monto: monto = 0 

    conn = get_db_connection()
    conn.execute(f"UPDATE pagos SET {mes} = ? WHERE id = ?", (monto, id_persona))
    conn.commit()
    conn.close()
    return redirect(url_for('index', mes=mes))

# NUEVA RUTA: SUBIR FOTO
@app.route('/subir_foto', methods=['POST'])
def subir_foto():
    id_persona = request.form['id']
    mes = request.form['mes']
    
    if 'foto' not in request.files:
        return redirect(request.url)
        
    file = request.files['foto']
    
    if file.filename == '':
        return redirect(request.url)

    if file:
        # Nombre único: id_mes_nombreoriginal.jpg
        filename = f"{id_persona}_{mes}_{secure_filename(file.filename)}"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # Guardar nombre en BD
        conn = get_db_connection()
        conn.execute(f"UPDATE pagos SET {mes}_foto = ? WHERE id = ?", (filename, id_persona))
        conn.commit()
        conn.close()

    return redirect(url_for('index', mes=mes))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')