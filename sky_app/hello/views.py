from flask import Blueprint, render_template, request
from sky_app.hello.models import MESSAGES

hello = Blueprint('hello',__name__)


@hello.route('/')
@hello.route('/hello')
def hello_sky():
    user = request.args.get('user','foscraft')
    return render_template('index.html',user=user)

    