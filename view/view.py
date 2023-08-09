class View:
    def show_message(self, message: str):
        print(message)

    def get_string(self, message: str) -> str:
        return input(message)

    def show_menu_get_answer(self, menu: str) -> int:
        try:
            res = int(input(menu))
            return res
        except ValueError as e:
            return -1
