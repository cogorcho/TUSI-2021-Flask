delete from ModHospitalaria
where length(PRIMARIA) = 0
and length(Secundaria) = 0
and length(inicial) = 0;
