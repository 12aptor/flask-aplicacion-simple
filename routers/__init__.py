from pathlib import Path
from os import listdir
from importlib import import_module

path = Path('./routers')

for module in listdir(path):
  if 'router' in module:
    import_module(
      f'routers.{module[:-3]}'
    )