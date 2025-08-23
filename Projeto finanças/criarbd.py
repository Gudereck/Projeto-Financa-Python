import sqlite3 as lite

con = lite.connect('dados.db')

with con:
    cur = con.cursor()

    # Tabela Categoria
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Categoria (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT
        )
    """)

    # Tabela Receitas
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Receitas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            categoria TEXT,
            adicionado_em DATE,
            valor DECIMAL
        )
    """)

    # Tabela Gastos
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Gastos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            categoria TEXT,
            retirado_em DATE,
            valor DECIMAL
        )
    """)

print("Tabelas criadas (ou já existentes).")
