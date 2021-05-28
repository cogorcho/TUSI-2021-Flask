create table Escuelas (
	 Jurisdiccion varchar(64) not null,
	 Sector varchar(32) not null,
	 Ambito varchar(32) not null,
	 Departamento varchar(128) not null,
	 CodDepartamento varchar(32) not null,
	 Localidad varchar(256) not null,
	 CodLocalidad varchar(132) not null,
	 CUE int not null,
	 CUAnexo int not null,
	 Nombre varchar(256) not null,
	 Domicilio varchar(512) not null,
	 CodPostal varchar(64) not null,
	 CodArea varchar(32) not null,
	 Telefono varchar(128) not null,
	 Email varchar(256) not null
)
