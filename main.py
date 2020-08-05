import time
from watchdog.observers import Observer

from handler import Handler

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
