# Willian Reichert - 09/09/2021
import sqlite3 as sq
import unicodedata

FILE = 'gerint.csv'
OPTIONS = '123456'

db = sq.connect(':memory:')

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

# TODO: verificações de entrada (opções e nomes)
option = input('Command [1 - 6]: ')

if (option == '1'):
    municipio = normalize(input('Informe o nome do município: ').upper())

    count = db.execute(f'SELECT COUNT(*) FROM internacoes WHERE municipio_residencia = "{municipio}"').fetchone()[0]
    print(f'Número de pacientes em {municipio.title()}: {count}')

    avg_age = [0] * 2
    for index, sex in enumerate(['MASCULINO', 'FEMININO']):
        avg_age[index] = db.execute(f'SELECT AVG(idade) FROM internacoes WHERE municipio_residencia = "{municipio}" AND sexo = "{sex}"').fetchone()[0]
    print(f'Média de idade de pacientes masculinos em {municipio.title()}: {avg_age[0]}')
    print(f'Média de idade de pacientes femininos em {municipio.title()}: {avg_age[1]}')

    print(f'Media de idade dos pacientes em {municipio.title()}: {sum(avg_age) / 2}')

elif (option == '2'):
    municipio = normalize(input('Informe o nome do município: ').upper())

    print(f'Internações por ano em {municipio.title()}:')
    for year in ['2018', '2019', '2020', '2021']:
        count = db.execute(f'SELECT COUNT(*) FROM internacoes WHERE municipio_residencia = "{municipio}" AND data_internacao LIKE "{year}%"').fetchone()[0]
        print(f'{year}: {count} internações')

# TODO: formatar
elif (option == '3'):
    executante = normalize(input('Informe o nome do hospital executante: ').upper())
    print(db.execute(f'SELECT id_usuario, municipio_residencia, solicitante, data_autorizacao, data_internacao, data_alta, executante FROM internacoes WHERE executante = "{executante}"').fetchall())

# TODO: cálculo com datas e lidar com pacientes ainda internados (data de alta == '')
elif (option == '4'):
    solicitante = normalize(input('Informe o nome do hospital solicitante: ').upper())
    print(db.execute(f'SELECT id_usuario, data_solicitacao, data_alta, executante FROM internacoes WHERE solicitante = "{solicitante}"').fetchall())

# TODO: formatar
elif (option == '5'):
    print(db.execute(f'SELECT horas_na_fila FROM internacoes ORDER BY horas_na_fila DESC LIMIT 5').fetchall())

elif (option == '6'):
    db.close()
    print('Quitting...')
    quit()
