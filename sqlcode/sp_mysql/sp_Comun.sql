--------------------------------------------
-- Escuelas de Comun
--------------------------------------------
DELIMITER //
DROP PROCEDURE IF EXISTS sp_Comun;

create procedure sp_Comun(IN jid INT)
BEGIN
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
        case when Maternal = 1 THEN 'Maternal,' ELSE '' end),
        case when Inicial = 1 THEN 'Inicial,' ELSE '' end),
        case when Primaria = 1 THEN 'Primaria,' ELSE '' end),
        case when Secundaria = 1 THEN 'Secundaria, ' ELSE '' end),
        case when Secundaria_Tecnica_INET = 1 THEN 'Secundaria Tecnica INET, ' ELSE '' end)
        As Niveles
from ModComun m
    inner join NEscuelas e
    on e.cue = m.cue
        and e.cueanexo = m.cueanexo
    inner join Localidad l
    on l.id = e.localidad_id
    inner join Departamento d
    on d.id = l.departamento_id
    inner join Jurisdiccion j
    on j.id = d.jurisdiccion_id
where j.id = jid;
END//

delimiter ;

--------------------------------------------
-- Escuelas de Comun Test
--------------------------------------------
--declare @jid int = 2
--exec sp_Comun @jid

--SET @jid = NULL
--exec sp_Comun @jid

--CUE                       | varchar(128) | NO   |     | NULL    |       |
--| CUEAnexo                  | varchar(128) | NO   |     | NULL    |       |
--| Maternal                  | varchar(128) | NO   |     | NULL    |       |
--| Inicial                   | varchar(128) | NO   |     | NULL    |       |
--| Primaria                  | varchar(128) | NO   |     | NULL    |       |
--| Secundaria                | varchar(128) | NO   |     | NULL    |       |
--| Secundaria_Tecnica_INET   | varchar(128) | NO   |     | NULL    |       |
--| Superior_No_Universitario | varchar(128) | NO   |     | NULL    |
