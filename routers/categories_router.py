from app import app
from controllers.categories_controller import CategoriesController
from flask import request

@app.route('/categories', methods=['GET', 'POST'])
def categoriesAll():
  controller = CategoriesController()
  if request.method == 'GET':
    return controller.getAll()
  else:
    return controller.create(request.json)