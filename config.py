import os

basedir = os.path.abspath(os.path.dirname(__file__))

# Ruta de la base de datos.
# Si DATABASE_PATH no está definida, utiliza app.db
# en el directorio del proyecto.
database_path = os.path.abspath(
    os.environ.get(
        "DATABASE_PATH",
        os.path.join(basedir, "app.db")
    )
)

# Crear el directorio de la base de datos si no existe.
os.makedirs(os.path.dirname(database_path), exist_ok=True)


class Config:
    # Configuración de SQLAlchemy
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{database_path}"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Clave secreta recibida desde el entorno.
    # El valor alternativo es únicamente para desarrollo.
    SECRET_KEY = os.environ.get("SECRET_KEY") or "dev-only-change-me"

    # Configuración de las cookies de sesión.
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"

    # Activar cuando el sitio se publica mediante HTTPS.
    SESSION_COOKIE_SECURE = (
        os.environ.get("SESSION_COOKIE_SECURE", "false").lower() == "true"
    )