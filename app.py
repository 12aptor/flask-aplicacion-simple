from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import BaseConfig
from flask_migrate import Migrate

app = Flask(__name__)

app.config.from_object(BaseConfig)

# SQLAlchemy es un ORM que nos permite interactuar con la base de datos, por ejemplo: crear tablas, inservar datos, crear, datos, etc
db = SQLAlchemy(app)

# Flask migrate nos sirve para hacer migraciones y modificar la base de datos.
migrate = Migrate(app, db)

# Aquí estamos importando nuestras rutas
# import routers.categories_router
# import routers.products_router

# Importar rutas segunda forma
import routers