create table Departamento (
	    id int not null auto_increment,
	    jurisdiccion_id int not null,
	    codigo varchar(32) not null,
	    nombre varchar(128) not null,
	primary key(id),
	    FOREIGN KEY (jurisdiccion_id) REFERENCES Jurisdiccion(id)
);

insert into Departamento(jurisdiccion_id,codigo,nombre)
select distinct j.id, e.CodDepartamento, e.Departamento
from Escuelas e
inner join Jurisdiccion j
  on j.nombre = e.Jurisdiccion;


select j.id, j.nombre, d.id, d.codigo, d.nombre
from Departamento d
inner join Jurisdiccion j
    on j.id = d.jurisdiccion_id;

