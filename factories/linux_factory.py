from factories.gui_factory import GUIFactory
from objects.linux_button import LinuxButton


class LinuxFactory(GUIFactory):
    def create_button(self):
        return LinuxButton()
