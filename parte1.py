#PARTE 1.1

# defino la URL a obtener datos
var url

# Obtengo los datos de la url
response = get(url)

# Hay que activar el javascript de la pagina para obtener el contenido.
active_javascrip(response)

# Se parsean los datos del response para obtener el HTML.
html = parse(response)

#defino el array donde se guardaran los datos
var array

#para cada tag a dentro del html hacer
for link in buscar_tag(a):

	# si el texto del tag contiene CVE-157
	if link.texto contiene 'CVE-157' donde

		#Agrego el link al arreglo
		agregar(link.href)
	end if
end for



#PARTE 1.2

# defino la URL a obtener datos
var url
# el dia de hoy
var hoy
#defino el array donde se guardaran los datos
var array

# Obtengo los datos de la url con el dia de hoy
response = get(url+hoy)

# Hay que activar el javascript de la pagina para obtener el contenido.
active_javascrip(response)

# Se parsean los datos del response para obtener el HTML.
html = parse(response)

#Busco class title3 que es la que indica cuales son constituciones, modificaciones y disoluciones
# la posicion 1 es para CONSTITUCION
# la posicion 2 es para MODIFICACION
# la posicion 3 es para DISOLUCION

posicion = buscar_posicion_class('title3')

#para cada tag a dentro del html hacer
for link in buscar_tag(td):

	# La posicion de constitucion es menor del td donde estoy y el td donde estoy es menor que la de modificacion
	if posicion(td) >= posicion[0] AND posicion(td) <= posicion[1]:
		#el href es de un pdf
		if href contiene 'pdf'
			#Agrego el link al arreglo
			agregar(link.href)
		end if
	end if
end for



#PARTE 1.3

# defino la URL a obtener datos
var url
#defino el array donde se guardaran los datos
var array

for fecha='01-01-2018' to fecha<='31-12-2018':

	# Obtengo los datos de la url con el dia de hoy
	response = get(url+hoy)

	# Hay que activar el javascript de la pagina para obtener el contenido.
	active_javascrip(response)

	# Se parsean los datos del response para obtener el HTML.
	html = parse(response)

	#para cada tag a dentro del html hacer
	for link in buscar_tag(a):
		#Agrego el link al arreglo
		agregar(link.href)
		end if
	end for

end for



#PARTE 1.4

# defino la URL a obtener datos
var url
#defino el array donde se guardaran los datos
var array

for fecha='01-01-2016' to fecha<='31-12-2016':

	# Obtengo los datos de la url con el dia de hoy
	response = get(url+hoy)

	# Hay que activar el javascript de la pagina para obtener el contenido.
	active_javascrip(response)

	# Se parsean los datos del response para obtener el HTML.
	html = parse(response)

	#para cada tag a dentro del html hacer
	for link in buscar_tag(a):
		#Agrego el link al arreglo
		agregar(link.href)
		end if
	end for

end for