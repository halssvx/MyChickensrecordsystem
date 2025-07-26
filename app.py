from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

DEFAULT_CHICKENS = [
    "George", "Fleur", "Devon", "Casey", "Marigold", "Apple Mint"
]

def init_db():
    conn = sqlite3.connect('chickens.db')
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS chickens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')
    # Insert default chickens only if empty
    cur.execute('SELECT COUNT(*) FROM chickens')
    count = cur.fetchone()[0]
    if count == 0:
        cur.executemany('INSERT INTO chickens (name) VALUES (?)',
                        [(name,) for name in DEFAULT_CHICKENS])
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('chickens.db')
    cur = conn.cursor()
    cur.execute('SELECT id, name FROM chickens')
    chickens = cur.fetchall()
    conn.close()
    return render_template('index.html', chickens=chickens)

@app.route('/add', methods=['POST'])
def add_chicken():
    name = request.form.get('name', '').strip()
    if name:
        conn = sqlite3.connect('chickens.db')
        cur = conn.cursor()
        cur.execute('INSERT INTO chickens (name) VALUES (?)', (name,))
        conn.commit()
        conn.close()
    return redirect(url_for('index'))

@app.route('/update/<int:id>', methods=['POST'])
def update_chicken(id):
    new_name = request.form.get('new_name', '').strip()
    if new_name:
        conn = sqlite3.connect('chickens.db')
        cur = conn.cursor()
        cur.execute('UPDATE chickens SET name = ? WHERE id = ?', (new_name, id))
        conn.commit()
        conn.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>', methods=['POST'])
def delete_chicken(id):
    conn = sqlite3.connect('chickens.db')
    cur = conn.cursor()
    cur.execute('DELETE FROM chickens WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
