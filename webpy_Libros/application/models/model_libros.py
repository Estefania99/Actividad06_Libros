import config as config # importa el archivo config

db = config.db # crea un objeto db del objeto db creado en config

'''
Metodo para seleccionar todos los registros de la tabla libro
'''
def select_libros():
    try:
        return db.select('libro') # Selecciona todos los registros de la tabla libro
    except Exception as e:
        print "Model select_libros Error {}".format(e.args)
        print "Model select_libros Message {}".format(e.message)
        return None

'''
Metodo para seleccionar un registro que coincida con el nombre dado
'''
def select_nombre(nombre_libro):
    try:
        return db.select('libro',where='nombre_libro=$nombre_libro', vars=locals())[0] # selecciona el primer registro que coincida con el nombre
    except Exception as e:
        print "Model select_nombre Error {}".format(e.args)
        print "Model select_nombre Message {}".format(e.message)
        return None

'''
Metodo para insertar un nuevo registro
'''
def insert_libros(nombre_libro,autor,genero,numero_paginas,numero_volumenes,editorial,anio_publicacion):
    try:
        return db.insert('libro', nombre_libro=nombre_libro,autor=autor,genero=genero,numero_paginas=numero_paginas,numero_volumenes=numero_volumenes,editorial=editorial,anio_publicacion=anio_publicacion) # inserta un registro en personas
    except Exception as e:
        print "Model insert_libros Error {}".format(e.args)
        print "Model insert_libros Message {}".format(e.message)
        return None

'''
Metodo para eliminar un registro que coincida con el nombre recibido
'''
def delete_libros(nombre_libro):
    try:
        return db.delete('libro', where='nombre_libro=$nombre_libro',vars=locals()) # borra un registro de libros
    except Exception as e:
        print "Model delete_libros Error {}".format(e.args)
        print "Model delete_libros Message {}".format(e.message)
        return None
def delete_personajes(nombre):
    try:
        return db.delete('personajes', where='nombre=$nombre',vars=locals()) # borra un registro de personajes
    except Exception as e:
        print "Model delete_personajes Error {}".format(e.args)
        print "Model delete_personajes Message {}".format(e.message)
        return None
'''
Metodo para actualizar o
'''
def update_libros(nombre_libro,autor,genero,numero_paginas,numero_volumenes,editorial,anio_publicacion): # actualiza los datos de la tabla 
    try:
        return db.update('libro', 
            autor=autor, 
            genero=genero,
            numero_paginas=numero_paginas,
            numero_volumenes=numero_volumenes,
            editorial=editorial,
            anio_publicacion=anio_publicacion,
            where='nombre_libro=$nombre_libro',
            vars=locals())
    except Exception as e:
        print "Model update_libros Error {}".format(e.args)
        print "Model update_libros Message {}".format(e.message)
        return None

