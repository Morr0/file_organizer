import sys
import time
from watchdog.observers import Observer

from handler import Handler

# Check that the folder to work on is provided as an argument
if (len(sys.argv) < 2):
    raise Exception("The path to watch must be provided");

path = sys.argv[1]

event_handler = Handler(path)
observer = Observer()
observer.schedule(event_handler, path)
observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
    
observer.join()
