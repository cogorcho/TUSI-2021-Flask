create table Sector (
	id int not null auto_increment,
	nombre varchar(128) not null,
	primary key (id)
);

create unique index uid_ambito on Sector(nombre);

insert into Sector(nombre)
select distinct Sector from Escuelas;

select * from Sector;

