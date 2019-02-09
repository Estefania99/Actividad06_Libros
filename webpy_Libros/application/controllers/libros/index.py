import web
import config as config


class Index:
    def __init__(self):
        pass

    def GET(self):  
        libros = config.model_libros.select_libros().list() # Selecciona todos los registros de libros
        return config.render.index(libros) # Envia todos los registros y renderiza index.html
