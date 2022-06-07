from Logging.logger import logger_app
import warnings
warnings.filterwarnings("ignore")

logFilepath = "logging_file/Log_File.txt"
logger_object = logger_app()

def Replaced_file(replace_word,replaced_by):
    logfile = open(logFilepath, mode='a')
    logger_object.log(logfile, 'Entered in Replaced_file method')
    try:
        f = open("example.txt", "r+")
        data = f.read()

        data = data.replace(replace_word, replaced_by)

        f.truncate(0)

        f.write(data)
        logger_object.log(logfile,"word replaced successfully" )
        f.close()
    except Exception as error:
        logger_object.log(logfile, 'Exception occurred in Replaced_file function. Exception message :  ' + str(error))
        logger_object.log(logfile, 'Exited from the Replaced_file function')
        logfile.close()