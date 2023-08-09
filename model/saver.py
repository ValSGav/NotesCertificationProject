import csv
import datetime
import os.path

from model.notebook import Notebook


class Saver:
    def __init__(self, notebook: Notebook):
        self.note_book = notebook

    def load_note_book(self, filename: str):
        try:
            if not os.path.exists(filename):
                file = open(filename, mode="tw")
                file.close()
            with open(filename, encoding="utf-8") as csv_file:
                fieldnames = ["note_id", "title", "body", "date_year", "date_month", "date_day"]
                reader = csv.DictReader(f=csv_file, fieldnames=fieldnames, delimiter="|")
                for row in reader:
                    note_id = int(row['note_id'])
                    body = row['body']
                    title = row['title']
                    date_year = row['date_year']
                    date_month = row['date_month']
                    date_day = row['date_day']
                    self.note_book.add_note(title, body, note_id,
                                            datetime.datetime(int(date_year),
                                                              int(date_month),
                                                              int(date_day)))
        except IOError as e:
            print(e)


    def save_note_book(self, filename: str):
        with open(filename, encoding="utf-8", mode="w") as csv_file:
            fieldnames = ["note_id", "title", "body", "date_year", "date_month", "date_day"]
            writer = csv.DictWriter(f=csv_file, fieldnames=fieldnames, delimiter="|")
            for key, value in self.note_book.get_notes().items():
                writer.writerow(dict(note_id=value.note_id, body=value.body, title=value.title, date_year=value.date.year,
                                 date_month=value.date.month, date_day=value.date.day))
