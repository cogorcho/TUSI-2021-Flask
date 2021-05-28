--------------------------------------------
-- Escuelas de Adultos
--------------------------------------------
DROP PROCEDURE IF EXISTS sp_Adultos
GO

create procedure sp_Adultos
    @jid INT
as
select
    e.id EscuelaID,
    e.nombre Nombre,
    l.nombre Localidad,
    j.nombre Provincia,
    concat(
    concat(
    concat(
    concat(
    concat(
        case when Primaria = 1 THEN 'Primaria,' ELSE '' end,
        case when EGB3 = 1 THEN 'EGB3,' ELSE '' end
    ),
        case when Secundaria = 1 THEN 'Secundaria,' ELSE '' end),
        case when Alfabetizacion = 1 THEN 'Alfabetización,' ELSE '' end),
        case when Formacion_Profesional = 1 THEN 'Formación Profesional,' ELSE '' end),
        case when Formacion_Profesional_INET = 1 THEN 'Formación Profesional (INET),' ELSE '' end)
        As Niveles
from ModAdultos m
    inner join NEscuelas e
    on e.cue = m.cue
        and e.cueanexo = m.cueanexo
    inner join Localidad l
    on l.id = e.localidad_id
    inner join departamento d
    on d.id = l.departamento_id
    inner join Jurisdiccion j
    on j.id = d.jurisdiccion_id
where j.id = COALESCE(@jid,j.id)
GO

--------------------------------------------
-- Escuelas de Adultos Test
--------------------------------------------
declare @jid int = 2
exec sp_Adultos @jid

declare @jid int = NULL
exec sp_Adultos @jid