import sqlite3

conexao = sqlite3.connect('gastos.db')

cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS gastos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao TEXT NOT NULL,
        valor REAL NOT NULL,
        data DATE NOT NULL
    )
''')

conexao.commit()

conexao.close()

print("Banco de dados e tabela 'gastos' criados com sucesso!")