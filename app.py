import sqlite3
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime


app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('gastos.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        descricao = request.form['descricao']
        valor = request.form['valor']
        data = datetime.now().strftime('%Y-%m-%d')

        conn = get_db_connection()
        conn.execute('INSERT INTO gastos (descricao, valor, data) VALUES (?, ?, ?)',
                     (descricao, valor, data))
        conn.commit()
        conn.close()
        
        return redirect(url_for('index'))

    conn = get_db_connection()
    gastos = conn.execute('SELECT * FROM gastos ORDER BY id DESC').fetchall()
    conn.close()
    
    return render_template('index.html', gastos=gastos)


@app.route('/deletar/<int:id>')
def deletar(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM gastos WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)