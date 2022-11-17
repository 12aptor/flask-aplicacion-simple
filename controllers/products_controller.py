from models.products_model import ProductsModel


class ProductsController:
  def __init__(self) -> None:
    self.model = ProductsModel

  def getAll(self):
    return 'Productos router'

  def create(self):
    pass

  def update(self):
    pass

  def delete(self):
    pass