from telegram.ext import Updater, CommandHandler, MessageHandler, Filters#libreria para programar  boot
import logging
import web #importar ,la libreria que se conecta con la BD

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Database connection
db = web.database(
    dbn = 'mysql',
    host = 'localhost',
    db = 'libros',
    user = 'aski',
    pw = 'ak.2019',
    port = 3306
    )

#Samm17_bot 
token = '725971404:AAGtugWkqnjOFxysVRrNfXOIBf63STiZ8cA'#serie numerica que esta en telegram 

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    username = update.message.from_user.username
    update.message.reply_text('Hola {} usa estos comandos:\n/info llave #busca_informacion'.format(username))#saludo inicial 

def help(bot, update):
    username = update.message.from_user.username
    update.message.reply_text('Hola {} usa estos comandos:\n/info llave #busca_informacion'.format(username))

def search(update):#busqueda
    text = update.message.text.split()#text.split se envia a esta variable y cada que se encuetra un espacio split los corta 
    username = update.message.from_user.username
    try:#proteger de un error 
        id_libro = int(text[1]) # cast para convertir str a int/RECIBE el id  del productodz
        print "Send info to {}".format(username)
        print "Key search {}".format(id_libro)
        result = db.select('libro', where='id_libro=$id_libro ', vars=locals())[0]#consulta#dame todos los productos con ese id vars locals para obtener la variable de afuera 
        print result
        respuesta =  "Nombre del libro:" + str(result.nombre_libro) + ", " +"\nAutor:"+ str(result.autor) + ", " + "\nGenero:"+str(result.genero)+ ", " + "\nNo.paginas:"+str(result.numero_paginas)+ ", " +"\nVolumenes:"+ str(result.numero_volumenes)+ ", " + "\nEditorial:"+str(result.editorial)+ ", " + "\nAnio de Publicacion:"+str(result.anio_publicacion)#concatenacion 
        #response = "Sending Info " + str(result[0]) + ", " + str(result[1]) + ", " + str(result[2])
        #print response
        update.message.reply_text('Hola {}\nEsta es la informacion del libro que buscas:\n{}'.format(username, respuesta))
    except Exception as e:
        print "Error: " + str(e.message)#muestra el error
        update.message.reply_text('La llave {} es incorreta'.format(id_libro))

def info(bot, update):
    search(update)#invocar 

def echo(bot, update):#repite lo que recibe contesta
    update.message.reply_text(update.message.text)#para que el boot responda 
    print update.message.text#imprime lo que mando el usuario
    print update.message.date#imprime la fecha 
    print update.message.from_user#impirme todos los dat0s 
    print update.message.from_user.username
    
def error(bot, update, error):#en caso de error 
    logger.warn('Update "%s" caused error "%s"' % (update, error))

    
def main():#metodo principal 
    try:
        print 'S.A.M.M. init token'
        
        updater = Updater(token)#donde se guarda lo que se escribe y sirve para conectarnos con telegram

        # Get the dispatcher to register handlers
        dp = updater.dispatcher#prepara todo para recibir mensajes y poder contestar 

        print 'S.A.M.M. init dispatcher'

        # on different commands - answer in Telegram
        dp.add_handler(CommandHandler("start", start))#llama la linea 24
        dp.add_handler(CommandHandler("help", help))#llama la linea 2ocho 
        dp.add_handler(CommandHandler("info", info))#info en comillas el que escribe el usurio        

        # on noncommand i.e message - echo the message on Telegram
        dp.add_handler(MessageHandler(Filters.text, echo))#agrega el filtro por si no hay comandos 

        # log all errors
        dp.add_error_handler(error)#atrapa errores y los muestra en la consola 

        # Start the Bot
        updater.start_polling()#actva al boot

        # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
        # SIGTERM or SIGABRT. This should be used most of the time, since
        # start_polling() is non-blocking and will stop the bot gracefully.
        print 'S.A.M.M. ready'#muestra el mensaje listo 
        updater.idle()#lo pone vigilar 
    except Exception as e:
        print "Error 100: ", e.message

if __name__ == '__main__':#metodo que se va a ejecutar 
    main()
#pip install -r requirements.txt 
#python-telegram-bot == 5.3.0