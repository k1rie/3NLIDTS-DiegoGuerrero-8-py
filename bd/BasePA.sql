-- Base de datos y tabla usadas por el Formulario Vr3 (Actividad 08)
CREATE DATABASE IF NOT EXISTS progavanzada;
USE progavanzada;

CREATE TABLE IF NOT EXISTS BasePA (
    Id        INT AUTO_INCREMENT PRIMARY KEY,
    Nombre    VARCHAR(50)  NOT NULL,
    Apellidos VARCHAR(50)  NOT NULL,
    Edad      INT          NOT NULL,
    Estatura  DECIMAL(4,2) NOT NULL,  -- metros, ej. 1.75
    Telefono  VARCHAR(10)  NOT NULL,
    Genero    VARCHAR(10)  NOT NULL
);
