import os
import json
import time
from threading import Thread
from typing import Callable


class FileWatcher(Thread):
    """Watches a commands.json file and triggers handler."""

    def __init__(self, path: str, handler: Callable[[dict], None]):
        super().__init__(daemon=True)
        self.path = path
        self.handler = handler
        self._last_mtime = 0

    def run(self):
        while True:
            try:
                mtime = os.path.getmtime(self.path)
                if mtime != self._last_mtime:
                    self._last_mtime = mtime
                    with open(self.path) as fh:
                        data = json.load(fh)
                    for cmd in data:
                        self.handler(cmd)
            except FileNotFoundError:
                pass
            time.sleep(1)
