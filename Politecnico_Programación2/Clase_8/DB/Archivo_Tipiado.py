from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) # Crear la aplicación Flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mibase.db' # Configurar la base de datos SQLite
db = SQLAlchemy(app)   # Crear la instancia de SQLAlchemy

class Productos(db.Model): # Definir el modelo de Productos
    id = db.Column(db.Integer, primary_key=True) # Clave primaria
    nombre = db.Column(db.String(80), nullable=False) # Nombre del producto
    precio = db.Column(db.Float, nullable=False) # Precio del producto


#Cargar
pd = Productos(nombre='Mause', precio=50) # Crear una instancia de Producto
db.session.add(pd) # Agregar el producto a la sesión
db.session.commit() # Confirmar la sesión para guardar en la base de datos

#Filtrar
Productos.query.filter_by(nombre= 'Mause').filter() # Consultar todos los productos en la base de datos

#Listar
productos = Productos.query.all() # Obtener todos los productos
for p in productos: # Iterar sobre los productos
    print(p.id, p.nombre, p.precio) # Imprimir el nombre y precio de cada producto
    
#Modificar
p = Productos.query.filter_by(nombre='Mause').first() # Obtener el primer producto con nombre 'Mause'
p = Productos.query.get(1) # Obtener el producto con id 1
p.precio = 3500 # Modificar el precio
db.session.commit() # Confirmar la sesión para guardar los cambios

#Eliminar
p = Productos.query.get(1) # Obtener el producto con id 1
db.session.delete(p) # Eliminar el producto de la sesión
db.session.commit() # Confirmar la sesión para guardar los cambios
