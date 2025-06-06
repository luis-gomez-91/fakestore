from flask import render_template, Blueprint, request, redirect, url_for, session
import requests
from app.config import get_conection

logout_bp = Blueprint('logout', __name__)

@logout_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login.login'))