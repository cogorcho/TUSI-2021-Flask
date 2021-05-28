create table Localidad(
	    id int not null auto_increment,
	    departamento_id int not null,
	    codigo varchar(256) not null,
	    nombre varchar(256) not null,
	primary key (id),
	    FOREIGN KEY (departamento_id) REFERENCES Departamento(id)
);

insert into Localidad(departamento_id,codigo,nombre)
select distinct d.id, e.CodLocalidad, e.Localidad
from Escuelas e
inner join Departamento d
    on d.nombre = e.departamento
    and d.codigo = e.CodDepartamento;

select j.id, j.nombre, d.id, d.codigo, d.nombre, l.codigo, l.nombre
from Localidad l
inner join Departamento d
    on d.id = l.departamento_id
inner join Jurisdiccion j
    on j.id = d.jurisdiccion_id;
