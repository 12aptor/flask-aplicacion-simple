from models.categories_model import CategoriesModel
from app import db


class CategoriesController:
  def __init__(self) -> None:
    self.model = CategoriesModel

  def getAll(self):
    try:
      categories = self.model.query.all()
      response = []
      for category in categories:
        response.append({
          'id': category.id,
          'name': category.name,
          'status': category.status
        })
      return {
        'data': response
      }, 200
    except Exception as e:
      return {
        'message': 'Ha ocurrido un error',
        'error': str(e)
      }, 500

  def create(self, data):
    try:
      # Aquí se envía la data a nuestro model
      category = self.model(data['name'])
      # Aquí se crear una sesion para poder guardar en la base de datos
      db.session.add(category)
      # Aquí se confirma que esos datos se guarden en la base de datos
      db.session.commit()
      return {
        'data': {
          'id': category.id,
          'name': category.name,
          'status': category.status
        }
      }, 201
    except Exception as e:
      # Si ha ocurrido algun erro eliminamos el registro de la sesion
      db.session.rollback()
      return {
        'message': 'Ha ocurrido un error',
        'error': str(e)
      }, 500