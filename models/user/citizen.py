from models.user.base import WS_UserBase 
from core.routes import get_tmp_filename
from core.filesystem import FileSystem
from core.console import console_log


class WS_Citizen(WS_UserBase):

    def __init__(self, user = None):
        console_log(f'init USER citizen: {user}', 3)
        user_id = 0
        if user and  hasattr(user, 'id'): user_id = user.id

        super().__init__(user_id)
        if not user: return
        self.role = "citizen"
        self.name = user.name
        self.chat_id = user.chat_id

