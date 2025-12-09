from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

API_SAMPLES_DIR = "api_samples"

class APIFolderWatcher(FileSystemEventHandler):
    def __init__(self, agent):
        self.agent = agent

    def on_any_event(self, event):
        if event.is_directory:
            return

        if event.src_path.endswith(".txt"):
            print("\n📌 Detected change in API samples:", event.src_path)
            print("🔄 Re-running pipeline...\n")
            time.sleep(1)
            self.agent.run()

def start_auto_update(agent):
    observer = Observer()
    handler = APIFolderWatcher(agent)
    observer.schedule(handler, API_SAMPLES_DIR, recursive=False)
    observer.start()

    print("👀 Watching api_samples/ for changes...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
