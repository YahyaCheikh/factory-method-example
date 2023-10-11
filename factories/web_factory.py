from factories.gui_factory import GUIFactory
from objects.web_button import WebButton
from objects.windows_button import WindowsButton


class WebFactory(GUIFactory):
    def create_button(self):
        return WebButton()