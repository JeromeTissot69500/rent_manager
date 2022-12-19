from flask import Flask
from config.config import Config
from bdd.database import db, migrate

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app,db)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()