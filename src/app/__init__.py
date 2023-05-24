from flask import Flask
from .routes import views

app = Flask(__name__)
app.register_blueprint(views.bp)
