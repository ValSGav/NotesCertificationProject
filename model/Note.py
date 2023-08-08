from datetime import datetime

class Note:

    def __init__(self, note_id: int, title="", body="", date=datetime(1900, 1, 1)):
        self.note_id = note_id
        self.title = title
        self.body = body
        self.date = date

    def fill_self(self, note):
        self.body = note.body
        self.title = note.title
        self.date = note.date
