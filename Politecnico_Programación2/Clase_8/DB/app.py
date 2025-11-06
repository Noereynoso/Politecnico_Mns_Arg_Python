from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mibase.db' 
db = SQLAlchemy(app)  

class Productos(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    nombre = db.Column(db.String(80), nullable=False)
    precio = db.Column(db.Float, nullable=False) 


#Cargar
pd = Productos(nombre='Mause', precio=50) 
db.session.add(pd) 
db.session.commit() 

#Filtrar
Productos.query.filter_by(nombre= 'Mause').filter() 

#Listar
productos = Productos.query.all() 
for p in productos: 
    print(p.id, p.nombre, p.precio)
    
#Modificar
p = Productos.query.filter_by(nombre='Mause').first() 
p = Productos.query.get(1) 
p.precio = 3500 
db.session.commit() 

#Eliminar
p = Productos.query.get(1) 
db.session.delete(p) 
db.session.commit() 
