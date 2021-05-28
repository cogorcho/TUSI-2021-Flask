--------------------------------------------
-- Escuelas de Comun
--------------------------------------------
DROP PROCEDURE IF EXISTS sp_Comun
GO

create procedure sp_Comun
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
    concat(
        case when Maternal = 1 THEN 'Maternal,' ELSE '' end,
        case when Inicial = 1 THEN 'Inicial,' ELSE '' end
    ),
        case when Primaria = 1 THEN 'Primaria,' ELSE '' end),
        case when Secundaria = 1 THEN 'Secundaria, ' ELSE '' end),
        case when Secundaria_Tecnica_INET = 1 THEN 'Secundaria Tecnica INET, ' ELSE '' end),
        case when Superior_No_Universitario = 1 THEN 'Superior No Universitario, ' ELSE '' end),
        case when Superior_No_Universitario_INET = 1 THEN 'Superior No Universitario INET,' ELSE '' end)
        As Niveles
from ModComun m
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
-- Escuelas de Comun Test
--------------------------------------------
declare @jid int = 2
exec sp_Comun @jid

SET @jid = NULL
exec sp_Comun @jid