from os import getenv

class BaseConfig:
  SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URI')