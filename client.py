from objects.linux_button import LinuxButton
from objects.windows_button import WindowsButton


class PageThatNeedsButton:
    def create_button(self, platform):
        if platform == "Windows":
            return WindowsButton()
        elif platform == "Linux":
            return LinuxButton()
