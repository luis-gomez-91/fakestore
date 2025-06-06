from flask import render_template, Blueprint, request, redirect, url_for, session
import requests
from app.config import get_conection

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['usuario']
        passw = request.form['clave']

        conection = get_conection()
        cursor = conection.cursor()
        cursor.execute("select * from users where username=%s  and password=%s;", (user, passw))
        datos = cursor.fetchall()

        session['actual_user'] = datos

        if datos:
            return redirect(url_for('products.products'))
        else:
            return render_template('login.html', error = "Credenciales incorrectas")
        
    else:
        return render_template('login.html')