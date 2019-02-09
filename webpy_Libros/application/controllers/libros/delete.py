import web
import config as config


class Delete:
    def __init__(self):
        pass

    def GET(self, nombre_libro): 
       libros = config.model_libros.select_nombre(nombre_libro) # Selecciona el registro que coincida con nombre
       return config.render.delete(libros) # Envia el registro y renderiza delete.html
    
    def POST(self, nombre_libro):
        formulario = web.input() # Crea un objeto formuario con los datos enviados con el formulario
        nombre_libro = formulario['nombre_libro'] # Obtine el nombre almacenado en el formulario
        config.model_libros.delete_libros(nombre_libro) # Borra el registro del nombre seleccionado
        raise web.seeother('/') # Redirecciona a raiz
