from core.wsrequest import WsRequest
from core.funcs import compose

class EventDispatcher():

    def __init__(html_request):
        self.clazz = ""
        self.method = ""
        self.args = ""


    """
    Execute an event with event code getted in request
    """
    def run(event_name, headers, message="", user=None):
        modulename, funcname = EventDispatcher.event_data(event_name)
        print("[DEBUG",f"modulename: {modulename}, funcname: {funcname}")
        func = EventDispatcher.func_by_reflection(modulename, funcname)
        print("[DEBUG",f"reflection function: {func}")
        if func: response =  func(user, headers, message)
        return response


    """
        1) Cargar el paquete (archivo), generando un espacio de nombres
        2) Obtener el módulo a partir del paquete (espacio de nombres)
        3) Obtener la función  a partir del módulo 
     """
    def func_by_reflection(packetname, funcname):
        modulename = packetname
        packetpath = f"events.{packetname}"
        namespace = __import__(packetpath)
        module = getattr(namespace, modulename)
        func = getattr(module, funcname)
        return func


    def event_data(event_name):
        module = ""
        funcname = ""

        if isinstance(event_name, str): segments = event_name.split('-') 
        if len(segments) == 2:
            module = segments[0] 
            funcname = event_name.replace('-', '_')

        return module,funcname 
