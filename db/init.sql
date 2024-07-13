CREATE TABLE IF NOT EXISTS productos (
    id SERIAL PRIMARY KEY,
    codigo VARCHAR(50) UNIQUE NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    descripcion VARCHAR(200),
    categoria VARCHAR(50),
    proveedor VARCHAR(50),
    precio_compra FLOAT,
    unidad_medida VARCHAR(20),
    imagen VARCHAR(200),
    estado VARCHAR(20) DEFAULT 'disponible',
    ubicacion VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    dni VARCHAR(8) UNIQUE NOT NULL,
    semestre VARCHAR(10),
    correo VARCHAR(50) NOT NULL,
    telefono VARCHAR(15)
);

CREATE TABLE IF NOT EXISTS pedidos (
    id SERIAL PRIMARY KEY,
    cliente VARCHAR(50) NOT NULL,
    fecha_pedido TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    detalles VARCHAR(500),
    estado VARCHAR(20) DEFAULT 'pendiente'
);

CREATE TABLE IF NOT EXISTS detalle_pedido (
    id SERIAL PRIMARY KEY,
    pedido_id INTEGER REFERENCES pedidos(id) ON DELETE CASCADE,
    producto_id INTEGER REFERENCES productos(id),
    cantidad INTEGER NOT NULL
);
