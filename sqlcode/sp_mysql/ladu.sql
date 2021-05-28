delete from ModAdultos
where length(Primaria) = 0
and length(EGB3) = 0
and length(Secundaria) = 0
and length(Alfabetizacion) = 0
and length(Formacion_Profesional) = 0
and length(Formacion_Profesional_INET) = 0;
