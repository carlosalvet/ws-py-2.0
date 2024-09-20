from core.filesystem import FileSystem
from models.session import Session
from core.routes import get_tmp_filename


def session_new(_user, _chat):
    session = Session()
    session.user = _user
    session.chat = _chat

    session.persist()
    return session


def session_destroy(_user, _chat):
    session = Session()
    session.user = _user
    session.chat = _chat

    session.destroy()

def session_update(_user, _chat, tmp_dir=''):
    print('[DEBUG]', 'session update ...', _user, _chat, end=' ')

    session = Session()
    session.user = _user
    session.chat = _chat
    print('[OK]')
    return session

