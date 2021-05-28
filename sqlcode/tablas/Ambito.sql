create table Ambito (
	id int not null auto_increment,
	nombre varchar(128) not null,
	primary key (id)
);

create unique index uid_ambito on Ambito(nombre);

insert into Ambito(nombre)
select distinct Ambito from Escuelas;

select * from Ambito;

