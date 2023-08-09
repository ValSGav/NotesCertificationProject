from array import array
from datetime import datetime

from model.note import Note


class Notebook:
    def __init__(self):
        self.notes = {}
        self.max_note_id = 0

    def add_note(self, title: str, body: str, note_id=-1, date=datetime(1900, 1, 1)):
        if note_id == -1:
            self.notes[self.max_note_id] = Note(body=body, title=title, note_id=self.max_note_id, date=datetime.now())
        else:
            self.notes[note_id] = Note(body=body, title=title, note_id=note_id, date=date)
        self._set_max_note_id_()

    def delete_note(self, note_id: int):
        del self.notes[note_id]
        self._set_max_note_id_()

    def update_note(self, note_id: int, note):
        self.notes.get(note_id).fill_self(note)

    def get_notes(self
                  , min_date=datetime(1900, 1, 1)
                  , max_time=datetime(3999, 12, 31)):
        return_dict = {}

        for item_key, item_value in self.notes.items():
            if min_date <= item_value.date <= max_time:
                return_dict[item_key] = item_value
        return return_dict

    def get_note(self, id: int) -> Note:
        return self.notes.get(id, Note(0, "", "", datetime.now()))

    def _set_max_note_id_(self):
        for item_key, item_value in self.notes.items():
            if item_value.note_id >= self.max_note_id:
                self.max_note_id = item_value.note_id + 1
