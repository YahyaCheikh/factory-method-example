from client import PageThatNeedsButton


def main():
    app = PageThatNeedsButton()
    win_button = app.create_button("Windows")
    linux_button = app.create_button("Linux")

    print(win_button.render())   # Output: Render a Windows button
    print(linux_button.render()) # Output: Render a Linux button

if __name__ == "__main__":
    main()