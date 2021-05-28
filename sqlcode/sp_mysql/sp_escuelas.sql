delimiter //
drop procedure if exists sp_Escuelas;

create procedure sp_Escuelas(IN jid INT)
BEGIN
select
	ne.id as ID,
	ne.nombre as Escuela,
        ne.cue as CUE,
	ne.cueanexo as CUEAnexo, 
        s.nombre as Sector, 
	a.nombre as Ambito, 
	l.nombre as Localidad,
	j.nombre as Provincia,
	ne.domicilio as Domicilio
from NEscuelas ne
inner join Sector s
	on s.id = ne.sector_id
inner join Ambito a
	on a.id = ne.ambito_id
inner join Localidad l
	on l.id = ne.localidad_id
inner join Departamento d
	on d.id = l.departamento_id
inner join Jurisdiccion j
	on j.id = d.jurisdiccion_id
where j.id =  jid
order by ne.nombre;
END//

delimiter ;
