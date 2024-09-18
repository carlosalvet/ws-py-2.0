import os


__events__ = ["events.session", "events.htmlrequest", "events.chat", "events.sessions", "events.chat", "events.message"]

CHAT_ID_MAX_SIZE = 320000


BASE_URL = "/home/carlos/proyectos-py/ws-chat2.0/app"
CHAT_DIR = '../private/chat-edomex/chat'
CACHE_DIR = '../private/var'


# Constantes en Petición del cliente
SECTION_SEPARATOR = "\n\n"
HEADER_SEPARTOR = "\n"
HEADER_NAME_SEPARATOR = ":"
    
CHAT_BASENAME = 'conversation.log'
CHAT_DATA_FILENAME = 'metadata.ini'
