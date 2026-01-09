import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('DROP TABLE IF EXISTS pagos')
    
    # AÑADIMOS COLUMNAS "_foto" (TEXTO) PARA CADA MES
    c.execute('''
        CREATE TABLE pagos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            paterno TEXT NOT NULL,
            nombre TEXT NOT NULL,
            
            enero REAL DEFAULT 0, enero_foto TEXT,
            febrero REAL DEFAULT 0, febrero_foto TEXT,
            marzo REAL DEFAULT 0, marzo_foto TEXT,
            abril REAL DEFAULT 0, abril_foto TEXT,
            mayo REAL DEFAULT 0, mayo_foto TEXT,
            junio REAL DEFAULT 0, junio_foto TEXT,
            julio REAL DEFAULT 0, julio_foto TEXT,
            agosto REAL DEFAULT 0, agosto_foto TEXT,
            septiembre REAL DEFAULT 0, septiembre_foto TEXT,
            octubre REAL DEFAULT 0, octubre_foto TEXT,
            noviembre REAL DEFAULT 0, noviembre_foto TEXT,
            diciembre REAL DEFAULT 0, diciembre_foto TEXT
        )
    ''')

    # Tus datos de siempre
    personas = [
        ("Suarez", "Reina"), ("Quispe", "Lidia"), ("Vertiz", "Valeria"), 
        ("Alvarez", "Cinthia"), ("Cumaly", "Fátima"), ("Pari", "Herminia"), 
        ("Canaviri", "Juan Carlos"), ("Quispe", "Sonia"), ("Aparicio", "Mauricio"), 
        ("Cruz", "Angelica"), ("Laura", "Justina"), ("Garcia", "Cnl."), 
        ("Huarachi", "Cap."),("Jimenez","Camila"), ("Quispe", "Diego"), ("Gutierrez", "Paola"), 
        ("Pinto", "Katherine"), ("Alvarez", "Francisco"), ("Ortiz", "Enrique"), 
        ("Zalles", "Claudia"), ("Vertiz", "Valeria"), ("Catari", "Ruben"), 
        ("Alvarez", "Cinthia"), ("Esprella", "Veronica"), ("Suarez", "Reina"), 
        ("Reyes", "Wilma")
    ]
    c.executemany('INSERT INTO pagos (paterno, nombre) VALUES (?, ?)', personas)
    conn.commit()
    conn.close()
    print("Base de datos actualizada con soporte para FOTOS.")

if __name__ == '__main__':
    init_db()