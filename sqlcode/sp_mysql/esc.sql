select
        cue,
	cueanexo, 
        s.nombre, 
	a.nombre, 
	ne.nombre,
	l.nombre,
	j.nombre
	ne.domicilio
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
where j.id =  22;
