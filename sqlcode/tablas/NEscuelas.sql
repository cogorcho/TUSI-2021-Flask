create table NEscuelas(
	    id int not null auto_increment,
	    cue int not null,
	    cueanexo int not null,
	    localidad_id int not null,
	    ambito_id int not null,
	    sector_id int not null,
	    nombre varchar(512) not null,
	    domicilio varchar(512) not null,
	    codpostal varchar(64),
	    codigoarea varchar(32),
	    telefono varchar(128),
	    email varchar(512),
	    PRIMARY KEY (id),
	    FOREIGN KEY (localidad_id) REFERENCES Localidad(id),
	    FOREIGN KEY (ambito_id) REFERENCES Ambito(id),
	    FOREIGN KEY (sector_id) REFERENCES Sector(id)
);


--create unique index uidx_NEscuelas_CUE on NEscuelas(cue, cueanexo);


insert into NEscuelas(
	cue,    
	cueanexo,    
	localidad_id,
	ambito_id,    
	sector_id,    
	nombre,
	domicilio,    
	codpostal,    
	codigoarea,
	telefono,    
	email
)
select 
	e.cue, 
	e.cuanexo, 
	l.id,
	a.id, 
	s.id, 
	e.nombre,
	ifnull(e.domicilio,'No diponible'), 
	e.codpostal, 
	e.codarea,
	e.telefono, 
	e.email
from Escuelas e
inner join Ambito a
    on a.nombre = e.ambito
inner join Sector s
    on s.nombre = e.sector
inner join Localidad l
    on l.nombre = e.Localidad
    and l.codigo = e.CodLocalidad
inner join Departamento d
    on d.id = l.departamento_id;




