from abc import ABC, abstractmethod

from observer import Observer


class Subject(ABC):
    @abstractmethod
    def register_observer(self, obs: Observer):
        pass

    @abstractmethod
    def remove_observer(self, obs: Observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass
