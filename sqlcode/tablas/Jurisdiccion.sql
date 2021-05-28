create table Jurisdiccion (
	id int not null auto_increment,
	nombre varchar(128) not null,
       	primary key(id)
);

create unique index uid_jurisdiccion on Jurisdiccion(nombre);

insert into Jurisdiccion(nombre)
select distinct Jurisdiccion from Escuelas
order by Jurisdiccion;

select * from Jurisdiccion;

