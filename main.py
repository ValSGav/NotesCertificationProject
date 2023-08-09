from controller.controller import Controller
from model.notebook import Notebook
from model.saver import Saver
from view.view import View

notebook = Notebook()
saver = Saver(notebook)
view = View()
controller = Controller(notebook=notebook, saver=saver, view=view)
controller.run()