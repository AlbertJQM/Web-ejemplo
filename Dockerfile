# Imagen base de Python
FROM python:3.13-slim

# Evitar la generación de archivos .pyc
# y mostrar los registros inmediatamente.
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Directorio de trabajo dentro del contenedor.
WORKDIR /app

# Copiar primero las dependencias.
COPY requirements.txt .

# Instalar dependencias.
RUN pip install --no-cache-dir -r requirements.txt

# Crear un usuario sin privilegios administrativos.
RUN groupadd --system --gid 10001 app \
    && useradd --system --uid 10001 \
       --gid app --home-dir /app --no-create-home app \
    && mkdir -p /app/data \
    && chown -R app:app /app

# Copiar el código de la aplicación.
COPY --chown=app:app . .

# Ejecutar como usuario no root.
USER app

# Puerto interno de Gunicorn.
EXPOSE 8000

# Ejecutar Flask con Gunicorn.
CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:8000", "app:app"]