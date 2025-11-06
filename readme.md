# ✅ Checklist para el Parcial de Programación II

### 1. Preparación inicial
- [ ] Crear carpeta del proyecto.  
- [ ] Inicializar repositorio con `git init`.  
- [ ] Subirlo a GitHub con un README.md.  

---

### 2. Backend con Python + Flask
- [ ] Crear archivo `app.py` con la configuración básica de Flask.  
- [ ] Definir rutas principales:  
  - `/nuevo` → formulario para cargar productos.  
  - `/productos` → lista de productos.  
  - `/eliminar/<id>` → borrar un producto.  
- [ ] Usar `render_template()` para conectar rutas con HTML.  

---

### 3. Modelado de datos con SQLAlchemy
- [ ] Definir clase `Producto` con atributos: `id`, `nombre`, `precio`, `imagen`.  
- [ ] Crear la base de datos y la tabla.  
- [ ] Insertar al menos 3 productos de prueba.  
- [ ] Implementar operaciones CRUD:  
  - Crear → `db.session.add()` + `commit()`.  
  - Leer → `Producto.query.all()`.  
  - Actualizar → modificar atributos + `commit()`.  
  - Eliminar → `db.session.delete()` + `commit()`.  

---

### 4. Frontend con HTML, CSS y Bootstrap
- [ ] Crear plantilla `nuevo.html` con formulario responsivo (nombre, precio, imagen).  
- [ ] Crear plantilla `productos.html` con tarjetas Bootstrap para mostrar productos.  
- [ ] Usar clases de Bootstrap para centrar, separar y dar estilo.  
- [ ] Probar en escritorio y en modo móvil.  

---

### 5. Plantillas dinámicas con Jinja2
- [ ] Recorrer lista de productos con `{% for producto in productos %}`.  
- [ ] Mostrar `{{ producto.nombre }}`, `{{ producto.precio }}`, `{{ producto.imagen }}`.  
- [ ] Usar condicionales si es necesario (`{% if %}`).  

---

### 6. Seguridad y buenas prácticas
- [ ] Validar datos de formularios (no dejar campos vacíos).  
- [ ] Usar `generate_password_hash()` si hay usuarios/contraseñas.  
- [ ] Organizar el código en funciones y archivos separados si es posible.  
- [ ] Comentar lo justo y mantener el código limpio.  

---

### 7. Pruebas y entrega
- [ ] Probar todas las rutas varias veces.  
- [ ] Insertar, listar, actualizar y eliminar productos.  
- [ ] Verificar que el diseño sea responsivo.  
- [ ] Subir cambios finales a GitHub con commits claros.  

---

# 🚀 Lenguajes y tecnologías que vas a usar
- **Python** (Flask + SQLAlchemy).  
- **HTML** (estructura).  
- **CSS + Bootstrap** (estilos y diseño responsivo).  
- **JavaScript (básico)** (validaciones simples o interactividad).  
- **SQL** (a través de SQLAlchemy).  
- **Git/GitHub** (control de versiones y entrega).  