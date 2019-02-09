import web
import config as config


class Update:
    def __init__(self):
        pass

    def GET(self, nombre_libro): 
        libros = config.model_libros.select_nombre(nombre_libro) # Selecciona el registro que coincida con nombre
        return config.render.update(libros) # Envia el registro y renderiza update.html
    
    def POST(self,libro):
        formulario = web.input() # almacena los datos del formulario web
        nombre_libro = formulario['nombre_libro'] # alamcena el nombre escrito en el input
        autor = formulario['autor'] # almacena el contenido escrito en el input
        genero = formulario['genero']
        numero_paginas = formulario['numero_paginas'] # alamcena la marca escrito en el input
        numero_volumenes = formulario['numero_volumenes'] # alamcena el precio escrito en el input
        editorial = formulario['editorial'] # alamcena la marca escrito en el input
        anio_publicacion = formulario['anio_publicacion'] # alamcena el precio escrito en el input
        config.model_libros.update_libros(nombre_libro,autor,genero,numero_paginas,numero_volumenes,editorial,anio_publicacion)
        raise web.seeother('/') # redirecciona al index

    
   