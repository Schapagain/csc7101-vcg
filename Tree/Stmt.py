from abc import ABC, abstractmethod

class Stmt(ABC):
    @abstractmethod
    def print(self):
        pass

    def _print(self, parent, child):
        self.print()
