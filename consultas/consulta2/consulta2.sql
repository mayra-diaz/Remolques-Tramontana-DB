SET SCHEMA 'RT1000';

-- Consulta no optimizada
SELECT SAMPLE1.nfactura, SAMPLE1.bdescripcion
FROM RT1000.bien SAMPLE, RT1000.compra SAMPLE1
WHERE SAMPLE.descripcion = SAMPLE1.bdescripcion AND
	  SAMPLE.clasificacion = 'Construcción' AND
	  SAMPLE.stock > 10 AND 
	  SAMPLE1.fecha BETWEEN '2019-01-01' and '2019-12-31' AND
	  SAMPLE1.preciounitario > 50;

-- 1000 tuplas

SET enable_mergejoin TO off;
SET enable_hashjoin TO off;
SET enable_bitmapscan TO off;
SET enable_sort TO off;

SELECT SAMPLE.nfactura, SAMPLE.bdescripcion
FROM 
((SELECT descripcion FROM RT1000.bien WHERE clasificacion = 'Construcción' AND stock > 0) SAMPLE1 
INNER JOIN RT1000.compra SAMPLE2 ON SAMPLE1.descripcion = SAMPLE2.bdescripcion) SAMPLE
WHERE SAMPLE.preciounitario > 50 AND SAMPLE.fecha BETWEEN '2019-01-01' and '2019-12-31';

CREATE INDEX bienClasificacion ON RT1000.bien USING Hash (clasificacion);
CREATE INDEX bienStock ON RT1000.bien (stock);
CREATE INDEX compraFecha ON RT1000.compra (fecha);
CREATE INDEX compraPrecioUnitario ON RT1000.compra (preciounitario);

-- Nro de bienes de la categoría construcción con stock mayor a 0: 24 

select * from RT1000.bien where clasificacion = 'Construcción' and stock > 0;

-- Compras de bienes de la categoría construcción con stock mayor a 0: 72

select * from RT1000.bien, RT1000.compra where clasificacion = 'Construcción' and stock > 0 and RT1000.bien.descripcion = RT1000.compra.bdescripcion;

-- Compras de bienes de la categoría construcción con stock mayor a 0 y precio unitario mayor a 50 entre las fechas requeridas: 6

select * from RT1000.bien, RT1000.compra where clasificacion = 'Construcción' and stock > 0 and RT1000.bien.descripcion = RT1000.compra.bdescripcion and preciounitario > 50 and fecha BETWEEN '2019-01-01' and '2020-01-01';

-- 10 000 tuplas

SET enable_mergejoin TO off;
SET enable_hashjoin TO off;
SET enable_bitmapscan TO off;
SET enable_sort TO off;

SELECT SAMPLE.nfactura, SAMPLE.bdescripcion
FROM 
((SELECT descripcion FROM RT10000.bien WHERE clasificacion = 'Construcción' AND stock > 0) SAMPLE1 
INNER JOIN RT10000.compra SAMPLE2 ON SAMPLE1.descripcion = SAMPLE2.bdescripcion) SAMPLE
WHERE SAMPLE.preciounitario > 50 AND SAMPLE.fecha BETWEEN '2019-01-01' and '2019-12-31';

CREATE INDEX bienClasificacion1 ON RT10000.bien USING Hash (clasificacion);
CREATE INDEX bienStock1 ON RT10000.bien (stock);
CREATE INDEX compraFecha1 ON RT10000.compra (fecha);
CREATE INDEX compraPrecioUnitario1 ON RT10000.compra (preciounitario);


-- Nro de bienes de la categoría construcción con stock mayor a 0: 404 

select * from RT10000.bien where clasificacion = 'Construcción' and stock > 0;

-- Compras de bienes de la categoría construcción con stock mayor a 0: 1212

select * from RT10000.bien, RT10000.compra where clasificacion = 'Construcción' and stock > 0 and RT10000.bien.descripcion = RT10000.compra.bdescripcion;

-- Compras de bienes de la categoría construcción con stock mayor a 0 y precio unitario mayor a 50 entre las fechas requeridas: 78

select * from RT10000.bien, RT10000.compra where clasificacion = 'Construcción' and stock > 0 and RT10000.bien.descripcion = RT10000.compra.bdescripcion and preciounitario > 50 and fecha BETWEEN '2019-01-01' and '2020-01-01';

-- 100 000 tuplas

SET enable_mergejoin TO off;
SET enable_hashjoin TO off;
SET enable_bitmapscan TO off;
SET enable_sort TO off;

SELECT SAMPLE.nfactura, SAMPLE.bdescripcion
FROM 
((SELECT descripcion FROM RT100000.bien WHERE clasificacion = 'Construcción' AND stock > 0) SAMPLE1 
INNER JOIN RT100000.compra SAMPLE2 ON SAMPLE1.descripcion = SAMPLE2.bdescripcion) SAMPLE
WHERE SAMPLE.preciounitario > 50 AND SAMPLE.fecha BETWEEN '2019-01-01' and '2019-12-31';

CREATE INDEX bienClasificacion2 ON RT100000.bien USING Hash (clasificacion);
CREATE INDEX bienStock2 ON RT100000.bien (stock);
CREATE INDEX compraFecha2 ON RT100000.compra (fecha);
CREATE INDEX compraPrecioUnitario2 ON RT100000.compra (preciounitario);


-- Nro de bienes de la categoría construcción con stock mayor a 0: 3843 

select * from RT100000.bien where clasificacion = 'Construcción' and stock > 0;

-- Compras de bienes de la categoría construcción con stock mayor a 0: 11529

select * from RT100000.bien, RT100000.compra where clasificacion = 'Construcción' and stock > 0 and RT100000.bien.descripcion = RT100000.compra.bdescripcion;

-- Compras de bienes de la categoría construcción con stock mayor a 0 y precio unitario mayor a 50 entre las fechas requeridas: 644

select * from RT100000.bien, RT100000.compra where clasificacion = 'Construcción' and stock > 0 and RT100000.bien.descripcion = RT100000.compra.bdescripcion and preciounitario > 50 and fecha BETWEEN '2019-01-01' and '2020-01-01';

-- 1 000 000 tuplas

SET enable_mergejoin TO off;
SET enable_hashjoin TO off;
SET enable_bitmapscan TO off;
SET enable_sort TO off;

SELECT SAMPLE.nfactura, SAMPLE.bdescripcion
FROM 
((SELECT descripcion FROM RT1000000.bien WHERE clasificacion = 'Construcción' AND stock > 0) SAMPLE1 
INNER JOIN RT1000000.compra SAMPLE2 ON SAMPLE1.descripcion = SAMPLE2.bdescripcion) SAMPLE
WHERE SAMPLE.preciounitario > 50 AND SAMPLE.fecha BETWEEN '2019-01-01' and '2019-12-31';

CREATE INDEX bienClasificacion3 ON RT1000000.bien USING Hash (clasificacion);
CREATE INDEX bienStock3 ON RT1000000.bien (stock);
CREATE INDEX compraFecha3 ON RT1000000.compra (fecha);
CREATE INDEX compraPrecioUnitario3 ON RT1000000.compra (preciounitario);


-- Nro de bienes de la categoría construcción con stock mayor a 0: 36872

select * from RT1000000.bien where clasificacion = 'Construcción' and stock > 0;

-- Compras de bienes de la categoría construcción con stock mayor a 0: 119616

select * from RT1000000.bien, RT1000000.compra where clasificacion = 'Construcción' and stock > 0 and RT1000000.bien.descripcion = RT1000000.compra.bdescripcion;

-- Compras de bienes de la categoría construcción con stock mayor a 0 y precio unitario mayor a 50 entre las fechas requeridas: 7478

select * from RT1000000.bien, RT1000000.compra where clasificacion = 'Construcción' and stock > 0 and RT1000000.bien.descripcion = RT1000000.compra.bdescripcion and preciounitario > 50 and fecha BETWEEN '2019-01-01' and '2020-01-01';