import signal
import threading
import time
from datetime import timedelta

from basis.scrapper import run_scrapper
from basis.mailing import send_email

TASK_EXECUTION_INTERVAL = 10  # seconds
NO_SLEEP_INTERVAL = 0  # seconds
TASK_EXECUTION_DELAY = 5  # seconds


class ProgramKilled(Exception):
    pass


def foo():
    print(time.ctime())


def signal_handler(signum, frame):
    raise ProgramKilled


class Job(threading.Thread):
    def __init__(self, interval, execute, *args, **kwargs):
        threading.Thread.__init__(self)
        self.daemon = False
        self.stopped = threading.Event()
        self.interval = interval
        self.execute = execute
        self.args = args
        self.kwargs = kwargs

    def stop(self):
        self.stopped.set()
        self.join()

    def run(self):
        while not self.stopped.wait(self.interval.total_seconds()):
            self.execute(*self.args, **self.kwargs)


def run_task(interval, func):
    if __name__ == "__main__":
        signal.signal(signal.SIGTERM, signal_handler)
        signal.signal(signal.SIGINT, signal_handler)
        job = Job(interval=timedelta(seconds=interval), execute=func)
        job.start()

    while True:
        try:
            time.sleep(NO_SLEEP_INTERVAL)
        except ProgramKilled:
            print("Program killed: stopping tasks")
            job.stop()
            break


#run_task(TASK_EXECUTION_INTERVAL, run_scrapper)
run_task(TASK_EXECUTION_INTERVAL + TASK_EXECUTION_DELAY, send_email)