from app import db
from sqlalchemy import Column, String, Integer, Boolean

class CategoriesModel(db.Model):
  __tablename__ = 'categories'

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(45), nullable=False)
  status = Column(Boolean, default=True)

  def __init__(self, name) -> None:
    self.name = name