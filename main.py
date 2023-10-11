from client import PageThatNeedsButton
from factories.linux_factory import LinuxFactory
from factories.windows_factory import WindowsFactory


def main():
    win_app = PageThatNeedsButton(WindowsFactory())
    linux_app = PageThatNeedsButton(LinuxFactory())

    win_button = win_app.create_button()
    linux_button = linux_app.create_button()

    print(win_button.render())   # Output: Render a Windows button
    print(linux_button.render()) # Output: Render a Linux button

if __name__ == "__main__":
    main()