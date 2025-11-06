import re
from pathlib import Path
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from models import db, User, Curso, PrecioHelper

USERNAME_RE = re.compile(r"^[A-Za-z0-9_\-.]{3,32}$")

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "dev-secret-please-change"
    instance_dir = Path(app.instance_path)
    instance_dir.mkdir(parents=True, exist_ok=True)
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{instance_dir/'app.db'}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    login_manager = LoginManager(app)
    login_manager.login_view = "login"

    @login_manager.user_loader
    def load_user(user_id):
        try:
            return User.query.get(int(user_id))
        except Exception:
            return None

    # Crear tablas y usuario por defecto
    with app.app_context():
        db.create_all()
        if not User.query.filter_by(username="politecnico").first():
            u = User(username="politecnico", role="admin")
            u.set_password("malvinas")
            db.session.add(u)
            db.session.commit()

    # Rutas
    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/acerca")
    def acerca():
        return render_template("acerca.html")

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            username = request.form.get("username","").strip()
            password = request.form.get("password","")
            if not username or not password:
                flash("Completá usuario y contraseña", "warning")
                return render_template("login.html")

            user = User.query.filter_by(username=username).first()
            if user and user.check_password(password):
                login_user(user)
                flash("Ingreso exitoso 👋", "success")
                return redirect(url_for("cursos_list"))
            flash("Usuario o contraseña inválidos", "danger")
        return render_template("login.html")

    @app.route("/register", methods=["GET", "POST"])
    def register():
        if request.method == "POST":
            username = request.form.get("username","").strip()
            password = request.form.get("password","")

            # Validaciones básicas lado servidor
            if not username or not password:
                flash("Completá usuario y contraseña", "warning")
                return render_template("register.html")

            if not USERNAME_RE.match(username):
                flash("Usuario inválido: 3-32 chars, letras, números, _-.", "warning")
                return render_template("register.html")

            if len(password) < 6:
                flash("La contraseña debe tener al menos 6 caracteres", "warning")
                return render_template("register.html")

            if User.query.filter_by(username=username).first():
                flash("Ese usuario ya existe", "danger")
                return render_template("register.html")

            user = User(username=username)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            flash("Registro exitoso. Ahora podés iniciar sesión.", "success")
            return redirect(url_for("login"))
        return render_template("register.html")

    @app.route("/logout")
    @login_required
    def logout():
        logout_user()
        flash("Sesión cerrada", "info")
        return redirect(url_for("index"))

    # --- CRUD de Cursos ---
    @app.route("/cursos")
    @login_required
    def cursos_list():
        q = request.args.get("q", "").strip().lower()
        cursos = Curso.query
        if q:
            cursos = cursos.filter(Curso.titulo.ilike(f"%{q}%"))
        cursos = cursos.order_by(Curso.id.desc()).all()
        return render_template("cursos_list.html", cursos=cursos, q=q)

    @app.route("/cursos/nuevo", methods=["GET", "POST"])
    @login_required
    def cursos_nuevo():
        if request.method == "POST":
            titulo = (request.form.get("titulo") or "").strip()
            descripcion = (request.form.get("descripcion") or "").strip()
            precio_raw = (request.form.get("precio") or "").strip()

            # Validaciones
            errores = []
            if not titulo:
                errores.append("El título es obligatorio.")
            if len(titulo) > 120:
                errores.append("El título no puede superar 120 caracteres.")
            try:
                precio_val = float(precio_raw.replace(",", "."))
                if precio_val < 0:
                    errores.append("El precio no puede ser negativo.")
            except ValueError:
                errores.append("El precio debe ser numérico.")

            if errores:
                for e in errores:
                    flash(e, "warning")
                return render_template("cursos_form.html", modo="nuevo",
                                       curso=dict(titulo=titulo, descripcion=descripcion, precio=precio_raw))

            helper = PrecioHelper(precio_val)
            precio_final = helper.con_descuento(0)
            c = Curso(titulo=titulo, descripcion=descripcion, precio=precio_final)
            db.session.add(c)
            db.session.commit()
            flash("Curso creado", "success")
            return redirect(url_for("cursos_list"))
        return render_template("cursos_form.html", modo="nuevo")

    @app.route("/cursos/<int:curso_id>/editar", methods=["GET", "POST"])
    @login_required
    def cursos_editar(curso_id):
        c = Curso.query.get_or_404(curso_id)
        if request.method == "POST":
            titulo = (request.form.get("titulo") or "").strip()
            descripcion = (request.form.get("descripcion") or "").strip()
            precio_raw = (request.form.get("precio") or "").strip()

            errores = []
            if not titulo:
                errores.append("El título es obligatorio.")
            if len(titulo) > 120:
                errores.append("El título no puede superar 120 caracteres.")
            try:
                precio_val = float(precio_raw.replace(",", "."))
                if precio_val < 0:
                    errores.append("El precio no puede ser negativo.")
            except ValueError:
                errores.append("El precio debe ser numérico.")

            if errores:
                for e in errores:
                    flash(e, "warning")
                return render_template("cursos_form.html", modo="editar", curso=c)

            c.titulo = titulo
            c.descripcion = descripcion
            c.precio = precio_val
            db.session.commit()
            flash("Curso actualizado", "success")
            return redirect(url_for("cursos_list"))
        return render_template("cursos_form.html", modo="editar", curso=c)

    @app.route("/cursos/<int:curso_id>/eliminar", methods=["POST"])
    @login_required
    def cursos_eliminar(curso_id):
        c = Curso.query.get_or_404(curso_id)
        db.session.delete(c)
        db.session.commit()
        flash("Curso eliminado", "info")
        return redirect(url_for("cursos_list"))

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
