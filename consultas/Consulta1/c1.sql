-- Cuántas horas trabajaron por máquina los empleados con los dos sueldos más altos del área de fabricación.

SET search_path TO RT1000;
--CREATE INDEX b_sueldo ON Empleado (sueldo);


EXPLAIN ANALYZE
SELECT sum(horas) AS HorasTotal
FROM (
	SELECT tfecha
	FROM (
		SELECT dni
		FROM (
			SELECT dni
				,sueldo
			FROM empleado
			WHERE area = 'Fabricacion'
			) F2
		WHERE sueldo IN (
				SELECT DISTINCT (sueldo)
				FROM (
					SELECT sueldo
					FROM empleado
					WHERE area = 'Fabricacion'
					) F
				ORDER BY sueldo DESC limit 2
				)
		) a
	INNER JOIN dirige d ON a.dni = d.dni
	) b
INNER JOIN trabajo t ON b.tfecha = t.fecha;

