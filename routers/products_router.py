from app import app
from controllers.products_controller import ProductsController

@app.route('/products')
def productsAll():
  controller = ProductsController()
  return controller.getAll()