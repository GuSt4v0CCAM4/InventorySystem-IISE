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

CREATE TABLE IF NOT EXISTS devoluciones (
    id SERIAL PRIMARY KEY,
    pedido_id INTEGER REFERENCES pedidos(id) ON DELETE CASCADE,
    fecha_devolucion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    estado_producto VARCHAR(20) NOT NULL,
    observaciones VARCHAR(500),
    responsable VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS notificaciones (
    id SERIAL PRIMARY KEY,
    usuario_id INTEGER REFERENCES usuarios(id) ON DELETE CASCADE,
    mensaje VARCHAR(500) NOT NULL,
    fecha_notificacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    estado VARCHAR(20) DEFAULT 'pendiente'
);
