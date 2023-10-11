class PageThatNeedsButton:
    def __init__(self, factory):
        self.factory = factory

    def create_button(self):
        return self.factory.create_button()
