-- Máquinas que hayan utilizado bienes medidos en kilogramos por una cantidad total mayor a 12.

SET SCHEMA 'RT';

SELECT F.mcodigo
FROM ( 
        (
            (
				SELECT descripcion
            	FROM RT.Bien
            	WHERE unidades='kg'
        	) as B 
        	INNER JOIN RT.Requiere R
			ON B.descripcion=R.bdescripcion
        ) AS O
        INNER JOIN (
            SELECT mcodigo, fecha, numero
            FROM RT.Trabajo
            WHERE fecha BETWEEN '2019-01-01' and '2020-01-01'
        ) AS T 
        ON (T.fecha=O.tfecha AND
           T.numero=O.tnumero)
) AS F
GROUP BY F.mcodigo
HAVING sum(F.cantidad) > 12;


-- Indices
-- Hash en B.unidades
SET enable_mergejoin TO off;
SET enable_hashjoin TO off;
SET enable_bitmapscan TO off;
SET enable_sort TO off;

CREATE INDEX bien_unidades ON RT.Bien USING Hash (unidades);
