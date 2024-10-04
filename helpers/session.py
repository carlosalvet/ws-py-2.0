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
    session = _SESSION[session_id]
    setattr(session, prop, 'Carlos')
    _SESSION[session_id] = session 


def session_new(session_id=0):
    global _SESSION

    session = Session()
    session.id = session_id 
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

