# Aplicacion simple con flask

## Variables de entorno

Debemos crear un archivo `.env` que contenga almenos estas dos variables de entorno.

```
FLASK_DEBUG = True

DATABASE_URI = 'mysql://root:root@localhost/flask_repaso'
```

## Migraciones

### Inicializar flask migrate (este comando se ejecuta una sola vez)
```bash
flask db init
```

### Crear los documentos de la migracion
```bash
flask db migrate -m "Initial migration"
```

### Ejecutar la migracion
```bash
flask db upgrade
```