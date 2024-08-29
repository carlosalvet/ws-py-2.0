from core.events import call_event 

# content of test_class.py
class TestClass:

    def test_one(self):
        REQUEST = "event:chat_converesation"
        call_event(null, REQUEST)

