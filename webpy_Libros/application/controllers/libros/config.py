import web # importa la libreria web.py
import application.models.model_libros as model_libros # importa el modelo_libros 


render = web.template.render('application/views/libros/', base='master') # configura la ubicacion de las vistas