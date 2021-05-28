DELIMITER //
DROP FUNCTION IF EXISTS fn_Provincia;

CREATE FUNCTION fn_Provincia( pid int )
RETURNS varchar(128)
BEGIN
	DECLARE pcianombre VARCHAR(128);

	SELECT nombre  INTO pcianombre
	FROM Jurisdiccion
	WHERE id = pid;

	RETURN pcianombre;

END; //


DELIMITER ;
