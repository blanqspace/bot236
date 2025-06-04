from threading import Thread
from typing import Callable


class TerminalCommand(Thread):
    """Thread that listens to terminal input."""

    def __init__(self, handler: Callable[[str], None]):
        super().__init__(daemon=True)
        self.handler = handler

    def run(self):
        while True:
            cmd = input()
            self.handler(cmd)
