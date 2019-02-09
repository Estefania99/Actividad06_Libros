CREATE DATABASE libros;

USE libros;

CREATE TABLE libro(
    id_libro int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre_libro varchar(100) NOT NULL,
    autor varchar(100) NOT NULL,
    genero varchar(100)  NOT NULL,
    numero_paginas int NOT NULl,
    numero_volumenes int  NULl,
    editorial varchar(100) NOT NULl,
    anio_publicacion int NOT NULl
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


INSERT INTO libro (nombre_libro,autor,Genero,numero_paginas,numero_volumenes,editorial,anio_publicacion)
VALUES ('La historia del loco','Jhon katzenbach','novela',544,0,'ZETA BOLSILLO',2004),
('El fetival de la blasfemia','Dross','terror',152,0,'Temas de Hoy',2016),
('It (Eso)','Stephen King','terror',1503,4,'debols!llo',1987);

SHOW TABLES;

SELECT * FROM libro;

DESCRIBE libros

CREATE USER 'aski'@'localhost' IDENTIFIED BY 'ak.2019';
GRANT ALL PRIVILEGES ON libros.* TO 'aski'@'localhost';
FLUSH PRIVILEGES;
