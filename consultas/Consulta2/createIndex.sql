CREATE INDEX bienClasificacion3 ON Bien USING Hash (clasificacion);
CREATE INDEX bienStock3 ON Bien (stock);
CREATE INDEX compraFecha3 ON Compra (fecha);
CREATE INDEX compraPrecioUnitario3 ON Compra (preciounitario);
