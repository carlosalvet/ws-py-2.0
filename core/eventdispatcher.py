from core.wsrequest import WsRequest
from core.funcs import compose

class EventDispatcher():


    """
    Execute an event with event code getted in request
    """
    @staticmethod
    def run(event_name, headers, message="", user=None):
        modulename, funcname = EventDispatcher._event_data(event_name)
        func = EventDispatcher._func_by_reflection(modulename, funcname)
        if func: response =  func(user, headers, message)
        return response


    """
        1) Cargar el paquete (archivo), generando un espacio de nombres
        2) Obtener el módulo a partir del paquete (espacio de nombres)
        3) Obtener la función  a partir del módulo 
     """
    @staticmethod
    def _func_by_reflection(packetname, funcname):
        print('[DEBUG]', 'Obteniendo función por reflexión:', end=' ')
        modulename = packetname
        packetpath = f"events.{packetname}"
        namespace = __import__(packetpath)
        module = getattr(namespace, modulename)
        func = getattr(module, funcname)
        print(func)
        return func


    @staticmethod
    def _event_data(event_name):
        print('[DEBUG]', 'Obtendiendo datos del event_name', end=' ')
        module = ""
        funcname = ""

        if isinstance(event_name, str): segments = event_name.split('-') 
        if len(segments) == 2:
            module = segments[0] 
            funcname = event_name.replace('-', '_')

        print('module: ', module, 'funcname: ', funcname, 'OK')
        return module,funcname 
