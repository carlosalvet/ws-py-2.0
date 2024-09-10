from core.wsrequest import WsRequest
from core.funcs import compose, console_log

class EventDispatcher():


    """
    Execute an event with event code getted in request
    """
    @staticmethod
    def run(event_code, body="", response_opened_conn=None):
        print('[DEBUG]', f'Event dispatcher. run event_code:{event_code}, body:{body}')
        modulename, eventname = EventDispatcher._event_sections(event_code)
        eventfunc = EventDispatcher._format_eventfunc(modulename, eventname)
        func = EventDispatcher._func_by_reflection(modulename, eventfunc)
        if func: response =  func(event_code, body, response_opened_conn)
        return response


    """
        1) Cargar el paquete (archivo), generando un espacio de nombres
        2) Obtener el módulo a partir del paquete (espacio de nombres)
        3) Obtener la función  a partir del módulo 
     """
    @staticmethod
    def _func_by_reflection(packetname, funcname):
        console_log('Obteniendo función por reflexión:', 1, ' ')
        modulename = packetname
        packetpath = f"events.{packetname}"
        namespace = __import__(packetpath)
        module = getattr(namespace, modulename)
        func = getattr(module, funcname)
        console_log(func)
        return func


    @staticmethod
    def _event_sections(event_name):
        console_log('Extrayendo datos del codigo del evento;', 1, ' ')
        module = ""
        funcname = ""

        #sbstr = substrings
        if isinstance(event_name, str): sbstr = event_name.split('-', 1)
        if len(sbstr) == 2:
            module = sbstr[0]
            event = sbstr[1]

        console_log(f'module: {module}, event: {event} OK', 1)
        return module, event 


    @staticmethod
    def _format_eventfunc(modulename, eventname):
        funcname = ""
        if modulename.isalnum() and eventname.isalnum():
            funcname =  f"{modulename}_{eventname}"
        return funcname
