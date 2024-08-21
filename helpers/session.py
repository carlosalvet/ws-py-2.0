from core.filesystem import FileSystem
from models.session import Session


def session_new(_user, _chat):
    session = Session()
    session.user = _user
    session.chat = _chat

    session.persist()
    return session
