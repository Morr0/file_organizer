from watchdog.events import FileSystemEventHandler
from watchdog.events import FileCreatedEvent

from mover import move_files

class Handler(FileSystemEventHandler):
    def __init__(self, path):
        super().__init__()

        self.path = path

    def on_created(self, event):
        if (type(event) is FileCreatedEvent):
            move_files(self.path)