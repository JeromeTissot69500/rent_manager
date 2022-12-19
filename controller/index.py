from flask import render_template, Blueprint

index_ws = Blueprint('index_ws',__name__,template_folder='templates')

@index_ws.get("/")
def index():
    return render_template("index.html")