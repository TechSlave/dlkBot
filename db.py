import sqlite3 as lite
from urllib.request import pathname2url
db = r'dlkbot.sqlite'


def create_db():
    try:
        dburi = f'file:{db}?mode=rw'
        conn = lite.connect(dburi, uri=True)

        print("Banco já existente, criação ignorada")
    except lite.OperationalError:
        conn = lite.connect(db)
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE produtos (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                chat_id INTEGER NOT NULL,
                modelo TEXT NOT NULL,
                codigo INTEGER NOT NULL,
                url TEXT NOT NULL,
                valor  INTEGER NOT NULL,
                disponivel INTEGER NOT NULL
        );
        """)
        print('Tabela criada com sucesso.')


def add_produto(chat_id, modelo, codigo, url, valor, disponivel):
    chat_id = int(chat_id)
    modelo = modelo
    codigo = int(codigo)
    url = url
    valor = int(valor)
    if disponivel:
        disponivel = 1
    else:
        disponivel = 0
    conn = lite.connect(db)
    cursor = conn.cursor()
    cursor.execute(f"""
    INSERT INTO produtos(chat_id, modelo, codigo, url, valor, disponivel)
    VALUES ('{chat_id}','{modelo}','{codigo}','{url}','{valor}','{disponivel}')
    """)
    conn.commit()

    print('Produto cadastrado com sucesso')
    conn.close()