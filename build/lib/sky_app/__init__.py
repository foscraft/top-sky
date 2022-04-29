from flask import Flask
from sky_app.hello.views import hello

app = Flask(__name__)
app.register_blueprint(hello)