select 
case Maternal when 1 then 'Si' Else 'No' End as Maternal,
case Inicial when 1 then 'Si' Else 'No' End as Inicial,
case Primaria when 1 then 'Si' Else 'No' End as Primaria,
case Secundaria when 1 then 'Si' Else 'No' End as Secundaria,
case Secundaria_Tecnica_INET when 1 then 'Si' Else 'No' End as Secundaria_Tecnica,
case Superior_No_Universitario when 1 then 'Si' Else 'No' End as Superior_No_Universitario
from ModComun;
