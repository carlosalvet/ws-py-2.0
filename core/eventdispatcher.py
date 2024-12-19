from core.wsrequest import WsRequest
from core.funcs import compose, get_extra_datum 
from core.console import console_log
import types

class EventDispatcher():


    """
    Execute an event with event code getted in request
    <ws://<address>:<port>/<extra-datum>
    """
    @staticmethod
    def call(event_code, body="", wsopen_data=None):
        response = ''
        ws_id = get_extra_datum(wsopen_data, 0, 'websocket_id')
        modulename, eventname = EventDispatcher._split(event_code)
        if modulename and eventname:
            func_name = EventDispatcher._format_functionname(modulename, eventname)
            func = EventDispatcher._get_func(modulename, func_name)
            response = EventDispatcher._exec(func, ws_id, body, wsopen_data)
        return response


    def _exec(func, ws_id, body, wsopen_data):
        if isinstance(func, types.FunctionType):
            response =  func(ws_id, body, wsopen_data)
        else:
            response = {'event':'', 'message':'', 'status': 500}
            response['message'] = f'La función no se puede ejecutar'

        return response


    """
        1) Cargar el paquete (archivo), generando un espacio de nombres
        2) Obtener el módulo a partir del paquete (espacio de nombres)
        3) Obtener la función  a partir del módulo 
     """
    @staticmethod
    def _get_func(packetname, funcname):
        modulename = packetname
        packetpath = f"events.{packetname}"
        namespace = __import__(packetpath)
        module = getattr(namespace, modulename)
        func = getattr(module, funcname)
        console_log(func)
        return func


    @staticmethod
    def _split(event_name):
        module = ""
        funcname = ""
        substr = 0
        module = ''
        event = ''

        #sbstr = substrings
        if isinstance(event_name, str): sbstr = event_name.split('-', 1)
        if len(sbstr) == 2:
            module = sbstr[0]
            event = sbstr[1]

        console_log(f'module: {module}, event: {event} OK', 1)
        return module, event 


    @staticmethod
    def _format_functionname(modulename, eventname):
        funcname = ""
        if modulename.isalnum() and eventname.isalnum():
            funcname =  f"{modulename}_{eventname}"
        console_log(f'nombre de la función: {funcname}', 1)
        return funcname
