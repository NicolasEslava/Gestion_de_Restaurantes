SHOW TABLES;

SHOW CREATE TABLE mesas;

CREATE TABLE productos (
    id_producto INT(11) NOT NULL AUTO_INCREMENT,
    nombre_producto VARCHAR(20) NOT NULL,
    descripcion VARCHAR(50) NULL,
    precio INT(20) NOT NULL,
    categoria VARCHAR(20) NOT NULL,
    estado VARCHAR(20) NOT NULL,
    PRIMARY KEY (id_producto),
    UNIQUE KEY (nombre_producto)
);

CREATE TABLE pedidos (
    id_pedido INT(11) NOT NULL AUTO_INCREMENT,
    id_mesa INT(11) NOT NULL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    estado VARCHAR(20) NOT NULL,
    observaciones VARCHAR(50) NULL,
    PRIMARY KEY (id_pedido),
    CONSTRAINT fk_id_mesas FOREIGN KEY (id_mesa) REFERENCES mesas (id_mesa)
);

CREATE TABLE detalle_pedido (
    id_detalle_pedido INT(11) NOT NULL AUTO_INCREMENT,
    id_pedido INT(11) NOT NULL,
    id_producto INT(11) NOT NULL,
    cantidad INT(20) NOT NULL,
    precio_unitario INT(11) NOT NULL,
    observaciones VARCHAR(50) NULL,
    PRIMARY KEY (id_detalle_pedido),
    CONSTRAINT fk_id_pedido FOREIGN KEY (id_pedido) REFERENCES pedidos (id_pedido),
    CONSTRAINT fk_id_producto FOREIGN KEY (id_producto) REFERENCES productos (id_producto)
);

ALTER TABLE productos MODIFY COLUMN precio DECIMAL(10, 2) NOT NULL;

ALTER TABLE detalle_pedido
MODIFY COLUMN precio_unitario DECIMAL(10, 2) NOT NULL;

INSERT INTO
    productos (
        nombre_producto,
        descripcion,
        precio,
        categoria,
        estado
    )
VALUES (
        'Hamburguesa Clasica',
        'Carne, queso, lechuga y tomate',
        18000.00,
        'Hamburguesas',
        'disponible'
    ),
    (
        'Hamburguesa BBQ',
        'Carne, queso, bacon y salsa BBQ',
        21000.00,
        'Hamburguesas',
        'disponible'
    ),
    (
        'Hamburguesa Especial',
        'Carne, queso, bacon y huevo',
        24000.00,
        'Hamburguesas',
        'disponible'
    ),
    (
        'Perro Caliente',
        'Salchicha, queso, papas y salsas',
        15000.00,
        'Perros',
        'disponible'
    ),
    (
        'Salchipapa',
        'Papas, salchicha y queso',
        16000.00,
        'Comidas',
        'disponible'
    ),
    (
        'Papas Fritas',
        'Papas fritas con salsa',
        7000.00,
        'Acompanamientos',
        'disponible'
    ),
    (
        'Pizza Personal',
        'Pizza de tamano personal',
        18000.00,
        'Pizzas',
        'disponible'
    ),
    (
        'Pizza Familiar',
        'Pizza de tamano familiar',
        32000.00,
        'Pizzas',
        'disponible'
    ),
    (
        'Gaseosa',
        'Bebida gaseosa 400 ml',
        5000.00,
        'Bebidas',
        'disponible'
    ),
    (
        'Agua',
        'Botella de agua 600 ml',
        4000.00,
        'Bebidas',
        'disponible'
    ),
    (
        'Jugo Natural',
        'Jugo natural de fruta',
        8000.00,
        'Bebidas',
        'disponible'
    ),
    (
        'Limonada',
        'Limonada natural',
        7000.00,
        'Bebidas',
        'disponible'
    );

INSERT INTO
    pedidos (
        id_mesa,
        estado,
        observaciones
    )
VALUES (
        1,
        'pendiente',
        'Pedido para mesa 1'
    ),
    (
        2,
        'preparando',
        'Pedido para mesa 2'
    ),
    (
        3,
        'listo',
        'Pedido para mesa 3'
    ),
    (
        4,
        'finalizado',
        'Pedido para mesa 4'
    ),
    (
        5,
        'pendiente',
        'Pedido para mesa 5'
    );

INSERT INTO
    detalle_pedido (
        id_pedido,
        id_producto,
        cantidad,
        precio_unitario,
        observaciones
    )
VALUES (
        1,
        1,
        2,
        18000.00,
        'Una sin cebolla'
    ),
    (1, 9, 2, 5000.00, NULL),
    (
        2,
        2,
        1,
        21000.00,
        'Agregar salsa BBQ'
    ),
    (2, 6, 1, 7000.00, NULL),
    (2, 10, 1, 4000.00, NULL),
    (3, 3, 2, 24000.00, NULL),
    (
        3,
        11,
        2,
        8000.00,
        'Jugo sin azucar'
    ),
    (4, 4, 1, 15000.00, NULL),
    (4, 5, 1, 16000.00, NULL),
    (5, 7, 1, 18000.00, NULL),
    (5, 12, 2, 7000.00, NULL);

SELECT * FROM mesas;

SELECT * FROM productos;

SELECT * FROM pedidos;

SELECT * FROM detalle_pedido;

SELECT p.id_pedido, p.id_mesa, pr.nombre_producto, d.cantidad, d.precio_unitario, (
        d.cantidad * d.precio_unitario
    ) AS subtotal
FROM
    pedidos p
    INNER JOIN detalle_pedido d ON p.id_pedido = d.id_pedido
    INNER JOIN productos pr ON d.id_producto = pr.id_producto;

SELECT * FROM productos WHERE id_producto = 5;

SELECT * FROM pedidos WHERE id_mesa = 1;

SELECT * FROM detalle_pedido;

SELECT id_pedido, id_mesa, estado
FROM pedidos
ORDER BY id_pedido DESC;

CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    rol ENUM('admin', 'mesero') NOT NULL,
    estado BOOLEAN DEFAULT TRUE
);

-- Insertar usuario Admin y Mesero iniciales (contraseñas 'admin123' y 'mesero123')
INSERT INTO
    usuarios (
        username,
        password_hash,
        nombre,
        rol
    )
VALUES (
        'admin',
        '$2b$12$eImiTXuWVxfM37uY4JANjO...hash_admin...',
        'Administrador Principal',
        'admin'
    ),
    (
        'mesero1',
        '$2b$12$eImiTXuWVxfM37uY4JANjO...hash_mesero...',
        'Carlos Mesero',
        'mesero'
    );