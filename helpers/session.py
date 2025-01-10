from core.filesystem import FileSystem
from models.session import Session
from core.routes import get_tmp_filename
from core.console import console_log

_SESSION = {}


def session_get(session_id=0):
    global _SESSION

    session = None
    console_log(f'Getting Session array: {_SESSION}', 2)
    if session_id in _SESSION: session = _SESSION[session_id]
    console_log(f'GET sessión al arreglo, session:{_SESSION}, session_id: {session_id}', 2)
    return session


def session_set(session_id, prop, value):
    global _SESSION

    session = _SESSION[session_id] if session_id in _SESSION else None
    if session and hasattr(session, 'prop'):
        setattr(session, prop, value)
        _SESSION[session_id] = session #Esta línea está de mas, por el apuntador
    else:
        return False 


def session_add(session, session_id):
    global _SESSION

    if not isinstance(session, Session):
        session = None
        console_log(f'La sesión que se intenta agregar no es válida: {session}', 4)
    else: 
        _SESSION[session_id] = session
        console_log(f'AGREGADO {session_id} a diccionario de sessiones:{_SESSION}', 3)


def session_remove(session_id, obj=None):
    global _SESSION

    is_str = isinstance(session_id, str)
    if is_str and session_id.is_digit(): session_id = int(session_id)
    if not isinstance(session_id, int): session_id = 0
    
    if session_id in _SESSION: _SESSION.pop(session_id)
    console_log(f'ELIMINADO {session_id} de diccionario de sesiones', 3)


def session_set_chat(session_id, chat):
    session = session_get(session_id)
    if session:
        session.chat = chat
        session.user.chat_id = chat.id
        session.persist()


'''
'''
def session_create(session_id=0, user=None, chat=None):
    session = Session()

    session_add(session, session_id)
    session_persist(session, session_id, user, chat)
    console_log(f'Create Sessión: {session}', 1)
    return session

def session_persist(session, session_id, user=None, chat=None):
    session.id = session_id 
    session.user = user
    session.chat = chat 
    session.persist()


def session_destroy(session_id):
    session = session_get(session_id)
    if session: 
        session.destroy()
        session_remove(session_id)

def session_update(session_id, _user=None, _chat=None):
    print('[DEBUG]', 'session update ...', _user, _chat, end=' ')
    session = session_get(session_id)
    session.user = _user
    session.chat = _chat

    print('[OK]')
    return session


def session_print_error(code=0):
    if code==0:
        console_log('', 1)
    elif code==1:
        console_log('helper session_new, session_id no existe', 4)
    else:
        console_log('Error desconocido', 1)
