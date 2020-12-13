-- Cuántas horas trabajaron por máquina los empleados con los dos sueldos más altos del área de fabricación.

set schema 'rt10000';
  
select sum(horas) as HorasTotal from 
(select tfecha from 
(select dni from (select dni, sueldo from empleado where area = 'Fabricacion') F2 where sueldo in 
	(select distinct(sueldo) from (select sueldo from empleado where area = 'Fabricacion') F order by sueldo desc limit 2)) a
	inner join dirige d on a.dni = d.dni) b inner join trabajo t on b.tfecha = t.fecha;

