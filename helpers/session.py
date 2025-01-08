from core.filesystem import FileSystem
from models.session import Session
from core.routes import get_tmp_filename
from core.console import console_log

_SESSION = {}


def session_get(session_id=0):
    global _SESSION
    console_log(f'Getting Session array: {_SESSION}', 1)
    session = None
    if session_id in _SESSION: session = _SESSION[session_id]
    return session


def session_set(session_id, prop, value):
    global _SESSION
    session = _SESSION[session_id] if session_id in _SESSION else None
    if session and hasattr(session, 'prop'):
        setattr(session, prop, value)
        _SESSION[session_id] = session #Esta línea está de mas, por el apuntador
    else:
        return False 


def session_set_chat(session_id, chat):
    session = session_get(session_id)
    if not session: return False
    session.chat = chat
    session.user.chat_id = chat.id
    session.persist()



def session_new(session_id=0, user=None):
    global _SESSION

    session = Session()
    session.id = session_id 
    session.user = user
    _SESSION[session_id] = session

    session.persist()
    console_log(f'Create Sessión: {session}', 1)
    return session


def session_destroy(session_id):
    global _SESSION
    session = _SESSION[session_id]
    session.destroy()

def session_update(session_id, _user, _chat=None):
    print('[DEBUG]', 'session update ...', _user, _chat, end=' ')
    session = session_get(session_id)
    session.user = _user
    if _chat: session.chat = _chat

    print('[OK]')
    return session

