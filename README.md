# 🛒 Proyecto Flask: Consumo de API FakeStore + MySQL

Este proyecto fue desarrollado como parte de la clase de Desarrollo Web en el Tecnológico. Utiliza **Flask** como framework backend para consumir la API pública [FakeStore API](https://fakestoreapi.com/) y almacenar algunos datos en una base de datos **MySQL**.

---

## 📌 Objetivos del Proyecto

- Conocer cómo consumir una API REST desde un backend en Python.
- Integrar Flask con MySQL para almacenar datos.
- Aplicar patrones MVC básicos.
- Practicar el manejo de rutas, templates, y conexión a servicios externos.
- Utilizar GitHub para versionar y compartir el proyecto.

---

## ⚙️ Tecnologías Utilizadas

- Python 3.11+
- Flask
- MySQL / MariaDB
- SQLAlchemy o PyMySQL (dependiendo de tu implementación)
- Jinja2 (templating)
- HTML/CSS básico
- [FakeStore API](https://fakestoreapi.com/)
- Git & GitHub

---

## 🛠 Pasos para Crear un Proyecto Flask

1. **Crear una carpeta del proyecto**
   ```bash
   mkdir proyecto-flask
   cd proyecto-flask
Inicializar entorno virtual

bash
Copiar
Editar
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
Instalar Flask

bash
Copiar
Editar
pip install flask
Crear archivo app.py

python
Copiar
Editar
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hola, mundo"

if __name__ == "__main__":
    app.run(debug=True)
Probar la aplicación

bash
Copiar
Editar
python app.py
Crear archivo requirements.txt

bash
Copiar
Editar
pip freeze > requirements.txt
📂 Estructura del Proyecto
arduino
Copiar
Editar
proyecto-flask/
├── app.py
├── config.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
├── models/
└── README.md
🚀 Cómo Ejecutar el Proyecto
bash
Copiar
Editar
python app.py
# o usando Flask CLI
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
🔌 Endpoints Principales
/ – Página principal que consume productos desde FakeStore API.

/producto/<id> – Detalles del producto.

/guardar/<id> – Guarda el producto en la base de datos.