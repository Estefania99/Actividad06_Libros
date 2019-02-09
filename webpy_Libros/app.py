import web
        
urls = (
    '/', 'application.controllers.libros.index.Index',
    '/insert', 'application.controllers.libros.insert.Insert',
    '/update/(.*)', 'application.controllers.libros.update.Update',
    '/delete/(.*)', 'application.controllers.libros.delete.Delete',
    '/view/(.*)', 'application.controllers.libros.view.View',
)

if __name__ == "__main__":
    web.config.debug = False
    app = web.application(urls, globals())
    app.run()
