from client import PageThatNeedsButton


def main():
    app = PageThatNeedsButton()
    win_button = app.create_button("Windows")
    linux_button = app.create_button("Linux")
    web_button = app.create_button("web")

    print(win_button.render())   # Output: Render a Windows button
    print(linux_button.render()) # Output: Render a Linux button
    print(web_button.render()) # Output: Render a Web button

if __name__ == "__main__":
    main()