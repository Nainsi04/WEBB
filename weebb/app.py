from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# SQLite database setup
conn = sqlite3.connect('contacts.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        message TEXT NOT NULL
    )
''')
conn.commit()
conn.close()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Insert data into the database
        conn = sqlite3.connect('contacts.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)', (name, email, message))
        conn.commit()
        conn.close()

        return redirect('/success')

    return redirect('/')


@app.route('/success')
def success():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)
