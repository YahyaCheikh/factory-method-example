from factories.gui_factory import GUIFactory
from objects.windows_button import WindowsButton


class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()
