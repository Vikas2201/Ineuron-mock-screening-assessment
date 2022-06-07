from Logging.logger import logger_app
from problem_1 import question_1
import warnings
warnings.filterwarnings("ignore")

logFilepath = "logging_file/Main_Log_File.txt"
logger_object = logger_app()
logfile = open(logFilepath, mode='a')

try:
    logger_object.log(logfile,'Entered in main.py python file')
    replace_word = input("Enter string that u want to replace : ")
    replaced_by = input("Enter Replaced string : ")
    question_1.Replaced_file(replace_word,replaced_by)
    logger_object.log(logfile, 'Replacement of string complete')

except Exception as error:
    logger_object.log(logfile, 'Exception occurred in main.py file. Exception message :  ' + str(error))
    logger_object.log(logfile, 'Exited from the file')
    logfile.close()