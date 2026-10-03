CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    rol ENUM('admin', 'mesero') NOT NULL,
    estado BOOLEAN DEFAULT TRUE
);

-- Insertar usuario Admin y Mesero iniciales (contraseñas 'admin123' y 'mesero123')
INSERT INTO usuarios (username, password_hash, nombre, rol) 
VALUES 
('admin', '$2b$12$eImiTXuWVxfM37uY4JANjO...hash_admin...', 'Administrador Principal', 'admin'),
('mesero1', '$2b$12$eImiTXuWVxfM37uY4JANjO...hash_mesero...', 'Carlos Mesero', 'mesero');