from flask import Blueprint, render_template


bp = Blueprint('main',__name__)

@bp.route('/')
@bp.route('/TahaElkhadir')
def index():
    """presentation de moi Taha el khadir  """
    return render_template('index.html',
                             title ='TahaElkhadir',
                             active_page='TahaElkhadir')

@bp.route('/cybersecurite')
def cybersecurity():
    """Page Cybersécurité & Pentesting"""
    return render_template('cybersecurity.html', 
                         title='Cybersécurité & Pentesting',
                         active_page='cybersecurite')

@bp.route('/developpement')
def development():
    """Page Développement Logiciel & IA"""
    return render_template('development.html', 
                         title='Développement Logiciel & IA',
                         active_page='developpement')