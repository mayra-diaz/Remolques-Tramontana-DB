SELECT SAMPLE.nfactura
	,SAMPLE.bdescripcion
FROM (
	(
		SELECT descripcion
		FROM.bien
		WHERE clasificacion = 'Construccion'
			AND stock > 0
		) SAMPLE1 INNER JOIN Ccompra SAMPLE2 ON SAMPLE1.descripcion = SAMPLE2.bdescripcion
	) SAMPLE
WHERE SAMPLE.preciounitario > 50
	AND SAMPLE.fecha BETWEEN '2019-01-01'
		AND '2019-12-31';