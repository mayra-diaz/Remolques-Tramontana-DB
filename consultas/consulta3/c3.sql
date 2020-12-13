-- Máquinas que hayan utilizado bienes medidos en kilogramos por una cantidad total mayor a 12.

SET SCHEMA 'RT1000';

SELECT T.mcodigo
FROM Trabajo T, Requiere R, Bien B
WHERE B.unidades='kg' AND T.fecha BETWEEN '2019-01-01' and '2020-01-01'
GROUP BY T.mcodigo
HAVING sum(R.cantidad) > 12;

-- Indices
-- Hash en B.unidades
CREATE INDEX 