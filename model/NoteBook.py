from array import array
from datetime import datetime

from Note import Note


class NoteBook:
    def __init__(self):
        self.notes = {}
        self.max_note_id = 0

    def add_note(self, title: str, body: str, note_id=-1, date=datetime(1900, 1, 1)):
        if note_id == -1:
            self.notes[self.max_note_id] = Note(body=body, title=title, note_id=note_id, date=date)
            self.max_note_id += 1
        else:
            self.notes[note_id] = Note(body=body, title=title, note_id=self.max_note_id, date=datetime.now())
            self._set_max_note_id_()

    def delete_note(self, note_id: int):
        del self.notes[note_id]
        self._set_max_note_id_()

    def update_note(self, note_id: int, note):
        self.notes.get(note_id).fillself(note)

    def get_notes(self
                  , min_date=datetime(1900, 1, 1)
                  , max_time=datetime(3999, 12, 31, 23, 59, 59)):
        return_dict = {}

        for item_key, item_value in self.notes:
            if min_date <= item_value.date <= max_time:
                return_dict[item_key] = item_value
        return return_dict

    def _set_max_note_id_(self):
        for item_key, item_value in self.notes:
            if item_value.note_id >= self.max_note_id:
                self.max_note_id = item_value.note_id + 1
