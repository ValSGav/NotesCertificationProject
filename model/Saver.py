import csv
import datetime

from NoteBook import NoteBook
from Note import Note


class Saver:
    def __init__(self):
        self.note_book = NoteBook()

    def load_note_book(self, filename: str):
        with open(filename, encoding="utf-8") as csv_file:
            fieldnames = ["note_id", "title", "body", "date_year", "date_month", "date_day"]
            reader = csv.DictReader(f=csv_file, fieldnames=fieldnames, delimiter="|")
            for row in reader:
                note_id = int(row["note_id"])
                body = row["body"]
                title = row["title"]
                date_year = row["date_year"]
                date_month = row["date_month"]
                date_day = row["date_day"]
                self.note_book.add_note(title, body, note_id,
                                        datetime.datetime(int(date_year),
                                                          int(date_month),
                                                          int(date_day)))
