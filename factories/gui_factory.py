from abc import ABC, abstractmethod


class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass