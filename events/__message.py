from helpers.chat import format_register

def message_send(session, headers, message):
    print("[PROCESS] events.message_send")
    print("[DEBUG] session.user", session, headers, message)

    is_authorize = session.user.authorize(session, str(headers['session-name']))
    response = ""
    if is_authorize:
        register = format_register(session, message)
        print(f"[DEBUG] session:{session}, message: {message}: register, {register}")
        session.chat.add_register(register)
        response = message

    return response 
    #format_message(session, message)
    #add_log (fmessage)
    print("al menos entró a esta madrinola")
