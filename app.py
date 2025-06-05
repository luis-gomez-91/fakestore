from flask import Flask, render_template, jsonify, request, redirect, url_for, blueprints
import requests
from config import get_conection

app = Flask(__name__)

@app.route('/')
def products():
    response = requests.get('https://fakestoreapi.com/products')
    data = response.json()
    return render_template('index.html', products = data)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['usuario']
        passw = request.form['clave']

        conection = get_conection()
        cursor = conection.cursor()
        cursor.execute("select * from users where username=%s  and password=%s;", (user, passw))
        datos = cursor.fetchall()

        if datos:
            return redirect(url_for('products'))
        else:
            return render_template('login.html', error = "Credenciales incorrectas")
        
    else:
        return render_template('login.html')