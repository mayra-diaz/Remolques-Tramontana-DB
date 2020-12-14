CREATE SCHEMA RT;

SET SCHEMA 'RT';

CREATE TABLE RT.Cliente(
  RUC bigint PRIMARY KEY,
  ubicacion varchar(100),
  razonSocial varchar(80) NOT NULL
);

CREATE TABLE RT.ContactoCliente (
  dni int PRIMARY KEY,
  nombre varchar(80) NOT NULL,
  celular int,
  correo varchar(60),
  ClienteRUC bigint NOT NULL,
  FOREIGN KEY(ClienteRUC) REFERENCES RT.Cliente(RUC),
  CONSTRAINT unique_ccl UNIQUE(celular)
);

CREATE TABLE RT.Proveedor(
  RUC bigint PRIMARY KEY,
  ubicacion varchar(100),
  razonSocial varchar(80) NOT NULL,
  descripcion varchar(150) NOT NULL,
  esDeProductoo boolean NOT NULL
);

CREATE TABLE RT.ContactoProveedor(
  dni int PRIMARY KEY,
  nombre varchar(80) NOT NULL,
  celular int,
  correo varchar(60),
  ProveedorRUC bigint NOT NULL,
  FOREIGN KEY(ProveedorRUC) REFERENCES RT.Proveedor(RUC),
  CONSTRAINT unique_pcl UNIQUE(celular)
);

CREATE TABLE RT.Empleado(
  dni int PRIMARY KEY,
  nombre varchar(80) NOT NULL,
  celular int NOT NULL,
  correo varchar(60) NOT NULL,
  direccion varchar(150) NOT NULL,
  nacimiento date NOT NULL,
  nCuenta bigint NOT NULL,
  area varchar(25) NOT NULL,
  cargo varchar(25) NOT NULL,
  sueldo double precision NOT NULL,
  CONSTRAINT unique_ecl UNIQUE(celular),
  CONSTRAINT unique_nCta UNIQUE(nCuenta)
);

CREATE TABLE RT.Maquina(
  codigo int PRIMARY KEY,
  descripcion varchar(150) NOT NULL
);

CREATE TABLE RT.Trabajo(
  fecha timestamp,
  numero smallint,
  descripcion varchar(150) NOT NULL,
  horas real NOT NULL,
  Mcodigo int NOT NULL,
  PRIMARY KEY(fecha, numero),
  FOREIGN KEY(Mcodigo) REFERENCES RT.Maquina(codigo)
);

CREATE TABLE RT.Dirige(
  dni int,
  Tfecha timestamp,
  Tnumero smallint,
  PRIMARY KEY(dni, Tfecha, Tnumero),
  FOREIGN KEY(dni) REFERENCES RT.Empleado(dni),
  FOREIGN KEY(Tfecha, Tnumero) REFERENCES RT.Trabajo(fecha, numero)
);

CREATE TABLE RT.Bien(
  descripcion varchar(100) PRIMARY KEY,
  esProducto boolean NOT NULL,
  unidades varchar(15) NOT NULL,
  stock smallint DEFAULT 0,
  clasificacion varchar(20) NOT NULL
);

CREATE TABLE RT.Compra(
  nFactura int,
  Bdescripcion varchar(100),
  fecha date NOT NULL,
  precioUnitario double precision NOT NULL,
  cantidad smallint NOT NULL,
  ProveedorRUC bigint NOT NULL,
  PRIMARY KEY(nFactura, Bdescripcion),
  FOREIGN KEY(Bdescripcion) REFERENCES RT.Bien(descripcion),
  FOREIGN KEY(ProveedorRUC) REFERENCES RT.Proveedor(RUC)
);

CREATE TABLE RT.Requiere(
  Bdescripcion varchar(100),
  Tfecha timestamp,
  Tnumero smallint,
  cantidad smallint NOT NULL,
  PRIMARY KEY(Bdescripcion, Tfecha, Tnumero),
  FOREIGN KEY(Bdescripcion) REFERENCES RT.Bien(descripcion),
  FOREIGN KEY(Tfecha, Tnumero) REFERENCES RT.Trabajo(fecha, numero)
);

CREATE TABLE RT.Carroceria(
  id serial PRIMARY KEY,
  placa varchar(8),
  vin varchar(20),
  categoria varchar(2) NOT NULL,
  carroceria varchar(25) NOT NULL,
  largo double precision NOT NULL,
  ancho double precision NOT NULL,
  alto double precision NOT NULL,
  nEjes smallint NOT NULL,
  nLlantas smallint NOT NULL,
  color varchar(15),
  cargaUtil double precision,
  pesoNeto double precision,
  ClienteRUC bigint NOT NULL,
  nFactura int,
  precio double precision,
  medioPago varchar(20),
  alContado boolean,
  fecha date NOT NULL,
  CONSTRAINT unique_placa UNIQUE(placa),
  CONSTRAINT unique_vin UNIQUE(VIN),
  FOREIGN KEY(ClienteRUC) REFERENCES RT.Cliente(RUC)
);

CREATE TABLE RT.Asociado(
  CarroceriaId int,
  CompraNFactura int,
  CompraBienDescripcion varchar(100),
  PRIMARY KEY(CarroceriaId, CompraNFactura, CompraBienDescripcion),
  FOREIGN KEY(CarroceriaId) REFERENCES RT.Carroceria(id),
  FOREIGN KEY(CompraNFactura, CompraBienDescripcion) REFERENCES RT.Compra(nFactura, Bdescripcion)
);
