import sqlite3 as sq
import unicodedata

FILE = 'gerint.csv'

class Database:
    def __init__(self):
        self.db = sq.connect(':memory:')
        self.fields = []
        self.field_count = 0

    def start(self):
        self.db.execute('''
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
            self.fields = file.readline().rstrip().split(';')
            print(self.fields)
            self.field_count = len(self.fields)
            idade_index = self.fields.index('idade')
            horas_index = self.fields.index('horas_na_fila')

            for line in file:
                data = line.rstrip().split(';')
                data = [normalize(item) for item in data]
                data[idade_index] = float(data[idade_index]) if data[idade_index] != '' else 0.0
                data[horas_index] = int(data[horas_index])
                self.db.execute(f'INSERT INTO internacoes VALUES ({"?, " * (self.field_count - 1)}?)', data)

            self.db.commit()

    def get(self):
        return self.db.execute('SELECT * FROM internacoes').fetchall()

    def close(self):
        self.db.close()

    def get_municipio(self, municipio: str):
        count = self.db.execute(f'SELECT COUNT(*) FROM internacoes WHERE municipio_residencia = "{municipio}"').fetchone()[0]
        print(f'Número de pacientes em {municipio.title()}: {count}')

        avg_age = [0] * 2
        for index, sex in enumerate(['MASCULINO', 'FEMININO']):
            avg_age[index] = self.db.execute(f'SELECT AVG(idade) FROM internacoes WHERE municipio_residencia = "{municipio}" AND sexo = "{sex}"').fetchone()[0]
        print(f'Média de idade de pacientes masculinos em {municipio.title()}: {avg_age[0]}')
        print(f'Média de idade de pacientes femininos em {municipio.title()}: {avg_age[1]}')

        print(f'Media de idade dos pacientes em {municipio.title()}: {sum(avg_age) / 2}')
        return self.db.execute(f'SELECT * FROM internacoes WHERE municipio_residencia = "{municipio}"').fetchall()
