# Usar la imagen oficial de PostgreSQL
FROM postgres:13

# Establecer las variables de entorno para la base de datos
ENV POSTGRES_DB=inventory_db
ENV POSTGRES_USER=admin
ENV POSTGRES_PASSWORD=secret

# Copiar el script de inicialización si es necesario
COPY init.sql /docker-entrypoint-initdb.d/
