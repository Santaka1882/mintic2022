import random

lambetazos = ["QUERIDOS", "APRECIADOS", "DISTINGUIDOS", "HONORABLES", "ESTIMADOS", "RESPETADOS"]
potenciales_marranos = ["COMPATRIOTAS", "CONCIUDADANOS", "AMIGOS", "COTERRANEOS", "COPARTIDARIOS", "ELECTORES"]
condiciones = ["EN MI GOBIERNO", "CON SU APOYO", "SIENDO ELEGIDO", "CON SU AYUDA", "SI ME SIGUEN", "DURANTE MI MANDATO"]
compromisos = ["VOY A DERROTAR", "VENCERÉ", "ELIMINARÉ", "ACABARÉ", "LUCHARÉ CONTRA", "COMBATIRÉ"]
iluciones_guerreristas = ["LA VIOLENCIA Y", "LA DELINCUENCIA Y", "LA CORRUPCION Y", "LA INFLACION Y", "LA POBBREZA Y", "EL DESPLAZAMIENTO Y"]
promesas = ["TRABAJARÉ POR", "GARANTIZARÉ", "PROTEGERÉ", "VELARÉ POR", "PROMEVERÉ", "DEFENDERÉ"]
beneficios_populistas =["LA EDUCACION", "EL EMPLEO", "LA SEGURIDAD", "LA PAZ", "LA IGUALDAD", "LA SALUD"]
cantidad_de_votos = ["DEL PAIS", "DE LA CIUDAD", "DE LA COMUNIDAD", "DE LA POBLACION", "PARA TODA LA GENTE", "DE CADA COLOMBIANO"]

lambetazo_seleccionado = random.choice(lambetazos)
marranos_seleccionados = random.choice(potenciales_marranos)
condicion_seleccionada = random.choice(condiciones)
compromiso_seleccionado = random.choice(compromisos)
ilucion_seleccionada = random.choice(iluciones_guerreristas)
promesa_seleccionada = random.choice(promesas)
populismo_seleccionado = random.choice(beneficios_populistas)
cantidad_seleccionada = random.choice(cantidad_de_votos)

print("El discurso final es: " + lambetazo_seleccionado + " " + marranos_seleccionados + " " + condicion_seleccionada + " " + compromiso_seleccionado + " " + ilucion_seleccionada + " " + promesa_seleccionada + " " + populismo_seleccionado + " " + cantidad_seleccionada)