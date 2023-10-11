from objects.linux_button import LinuxButton
from objects.web_button import WebButton
from objects.windows_button import WindowsButton


class PageThatNeedsButton:
    def create_button(self, platform):
        if platform == "Windows":
            return WindowsButton()
        elif platform == "Linux":
            return LinuxButton()
        elif platform == "Web":
            return WebButton()
