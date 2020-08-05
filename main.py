import time
from watchdog.events import FileSystemEventHandler
from watchdog.events import FileCreatedEvent
from watchdog.observers import Observer

class Handler(FileSystemEventHandler):
    def on_created(self, event):
        if (type(event) is FileCreatedEvent):
            print("File created")


event_handler = Handler()
observer = Observer()
observer.schedule(event_handler, ".")
observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
    
observer.join()
