import sqlite3 as sq
import unicodedata

FILE = 'gerint.csv'
db = sq.connect(':memory:')

def start():
    db.execute('''
        CREATE TABLE IF NOT EXISTS internacoes
        (
            data_extracao TEXT,
            id_usuario TEXT,
            situacao TEXT,
            central_regulacao_origem TEXT,
            data_solicitacao TEXT,
            sexo TEXT,
            idade REAL,
            municipio_residencia TEXT,
            solicitante TEXT,
            municipio_solicitante TEXT,
            codigo_cid TEXT, carater TEXT,
            tipo_internacao TEXT,
            tipo_leito TEXT,
            data_autorizacao TEXT,
            data_internacao TEXT,
            data_alta TEXT,
            executante TEXT,
            horas_na_fila INTEGER
        )'''
    )

    def normalize(word):
        return unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('ascii')

    with open(FILE, 'r', encoding='utf-8') as file:
        fields = file.readline().rstrip().split(';')
        field_count = len(fields)
        idade_index = fields.index('idade')
        horas_index = fields.index('horas_na_fila')

        for line in file:
            data = line.rstrip().split(';')
            data = [normalize(item) for item in data]
            data[idade_index] = float(data[idade_index]) if data[idade_index] != '' else 0.0
            data[horas_index] = int(data[horas_index])
            db.execute(f'INSERT INTO internacoes VALUES ({"?, " * (field_count - 1)}?)', data)

        db.commit()

def get():
    return db.execute('SELECT * FROM internacoes').fetchall()

def close():
    db.close()
