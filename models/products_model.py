from app import db
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class ProductsModel(db.Model):
  __tablename__ = 'products'

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(100), nullable=False)
  price = Column(Float, nullable=False)
  status = Column(Boolean, default=True)

  category_id = Column(Integer, ForeignKey('categories.id'))
  category = relationship('CategoriesModel')