from client import PageThatNeedsButton
from factories.linux_factory import LinuxFactory
from factories.web_factory import WebFactory
from factories.windows_factory import WindowsFactory


def main():
    win_app = PageThatNeedsButton(WindowsFactory())
    linux_app = PageThatNeedsButton(LinuxFactory())
    web_app = PageThatNeedsButton(WebFactory())

    win_button = win_app.create_button()
    linux_button = linux_app.create_button()
    web_button = web_app.create_button()

    print(win_button.render())   # Output: Render a Windows button
    print(linux_button.render()) # Output: Render a Linux button
    print(web_button.render()) # Output: Render a Web button

if __name__ == "__main__":
    main()