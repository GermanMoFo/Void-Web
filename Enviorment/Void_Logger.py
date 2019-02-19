#This file is meant to allow easy alterations to the format of logged messages
#mostly just abstracts the logging library but adds a DateTime to every message

import logging
import datetime

logging.basicConfig(filename='Void_Web.log', level=logging.DEBUG)

#Simple Interface Functions For Logging Use In Other Files
def Void_Log_Debug(message):
    __Log__(message, logging.debug)

def Void_Log_Info(message):
    __Log__(message, logging.info)

def Void_Log_Warning(message):
    __Log__(message, logging.warning)

def Void_Log_Error(message):
    __Log__(message, logging.error)

def Void_Log_Critical(message):
    __Log__(message, logging.critical)

#Formats messages to have standardized information added
def __Format_Message__(message):
    DT = str(datetime.datetime.now())
    formated = DT + " - " + message
    return formated

#Runs the log statements
def __Log__(message, logger):
    log = __Format_Message__(message)
    logger(log)