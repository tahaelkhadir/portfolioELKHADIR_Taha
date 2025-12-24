import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-taha-portfolio-2025'
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    