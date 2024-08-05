class WS_Visual():

    def __init__(self, _id=0, _chat_id=0):
        self.id = _id
        self.role = "visual"
        self.chat_id = _chat_id

    def to_string(self):
        string = f"id:{self.id},chat id:{self.chat_id},role:{self.role}"
        return string

    def get_persist_content(self):
        string = f"id:{self.id}\nrole:{self.role}\nchat id:{self.chat_id},"
        return string
