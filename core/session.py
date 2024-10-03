_SESSION = {}


def get_session(session_id=0):
    session = None
    if session_id in _SESSION:
        session = _SESSION[session_id]
    return session
