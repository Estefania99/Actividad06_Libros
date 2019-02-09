import web
import config as config


class View:
    def __init__(self):
        pass

    def GET(self, nombre_libro):  
        libros = config.model_libros.select_nombre(nombre_libro) # Selecciona el registro que coincida con nombre
        return config.render.view(libros) # Envia el registro y renderiza view.html
