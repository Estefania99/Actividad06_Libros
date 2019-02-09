import web
import config as config


class Insert:
    def __init__(self):
        pass

    def GET(self):  
        return config.render.insert() # renderiza la pagina insert.html
    
    def POST(self):
        formulario = web.input() # almacena los datos del formulario
        nombre_libro = formulario['nombre_libro'] # alamcena el nombre escrito en el input
        autor = formulario['autor'] # almacena el autr escrito en el input
        genero = formulario['genero'] # alamcena el genero escrito en el input
        numero_paginas= formulario['numero_paginas'] # almacena el numero de paginas escrito en el input
        numero_volumenes= formulario['numero_volumenes'] # almacena el numero de volumenes  escrito en el input
        editorial= formulario['editorial'] # almacena la editorial escrito en el input
        anio_publicacion= formulario['anio_publicacion'] # almacena el anio de publicacion  escrito en el input
        config.model_libros.insert_libros(nombre_libro,autor,genero,numero_paginas,numero_volumenes,editorial,anio_publicacion) # llama al metodo insert_datos y le paso los datos guardados
        raise web.seeother('/') # redirecciona al index.html
