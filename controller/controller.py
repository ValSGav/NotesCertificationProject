import datetime

from model.note import Note
from model.notebook import Notebook
from model.saver import Saver
from view.view import View
from config import db_name


def check_date(dateString: str) -> bool:
    if (len(dateString) == 10
            and dateString[0:2].isalnum()
            and dateString[3:5].isalnum()
            and dateString[6:10].isalnum()):
        return True
    else:
        return False


class Controller:

    def run(self):
        notebook = Notebook()
        saver = Saver(notebook)
        view = View()

        saver.load_note_book(db_name)

        isExit = False

        while not isExit:
            answer = view.show_menu_get_answer("""
            1- Add note
            2- Delete note
            3- Update Note
            4- Show note
            5- Exit
            """)

            if answer == 1:
                title = view.get_string("Введите заголовок заметки: ")
                body = view.get_string("Введите текст заметки: ")
                notebook.add_note(title, body)
                view.show_message("Заметка добавлена.")
                saver.save_note_book(db_name)
            elif answer == 2:
                try:
                    id = int(view.get_string("Введите номер заметки для удаления: "))
                    old_note = notebook.get_note(id)
                    if old_note.note_id == 0:
                        view.show_message(f"Не найдена заметка с номером {id}")
                    else:
                        notebook.delete_note(id)
                        saver.save_note_book(db_name)
                except ValueError as e:
                    print(e)
            elif answer == 3:
                try:
                    id = int(view.get_string("Введите номер заметки для обновления информации: "))
                    old_note = notebook.get_note(id)
                    if old_note.note_id == 0:
                        view.show_message(f"Не найдена заметка с номером {id}")
                    else:
                        title = view.get_string("Введите  новый заголовок заметки: ")
                        body = view.get_string("Введите новый текст заметки: ")
                        notebook.update_note(id, Note(old_note.note_id, title, body, old_note.date))
                        saver.save_note_book(db_name)
                except ValueError as e:
                    print(e)
            elif answer == 4:
                try:
                    dataStringMin = view.get_string("Введите дату начала отбора записей(в формате дд-мм-гггг)");
                    dataStringMax = view.get_string("Введите дату окончания отбора записей(в формате дд-мм-гггг)");

                    if(check_date(dataStringMin) and check_date(dataStringMax)):
                        dateMin = datetime.datetime.strptime(dataStringMin, '%d-%m-%Y')
                        dateMax = datetime.datetime.strptime(dataStringMax, '%d-%m-%Y')

                        dict_of_notes = notebook.get_notes(min_date=dateMin, max_time=dateMax)
                        for key, val in dict_of_notes.items():
                            view.show_message("{} - {}".format(key, val))
                    elif dataStringMin == "" and dataStringMax == "":
                        dict_of_notes = notebook.get_notes()
                        for key, val in dict_of_notes.items():
                            view.show_message("{} - {}".format(key, val))
                    else:
                        view.show_message("Даты должны соотвествовать формату дд-мм-гггг")
                except ValueError as e:
                    print(e)
            elif answer == 5:
                isExit = True

