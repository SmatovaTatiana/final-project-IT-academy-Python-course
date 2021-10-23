import datetime
import signal
import threading
import time
from datetime import datetime
from datetime import timedelta

from basis.scheduler import run_scheduled_jobs

TASK_DELAY_INTERVAL_24_HOURS = 86400   # seconds, for production
TASK_DELAY_INTERVAL_10_MINUTES = 600    # for debug
TASK_NO_DELAY_INTERVAL = 0    # seconds
SLEEP_INTERVAL = 5  # seconds
START_AT_HOUR = 00
START_AT_MINUTE = 10


class ProgramKilled(Exception):
    pass


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
    print("Timer: run task started at ", datetime.now(), '.\n')
    if __name__ == "__main__":
        signal.signal(signal.SIGTERM, signal_handler)
        signal.signal(signal.SIGINT, signal_handler)
        job = Job(interval=timedelta(seconds=interval), execute=func)

        # while datetime.now().time().hour != START_AT_HOUR or datetime.now().time().minute != START_AT_MINUTE:
        #    time.sleep(SLEEP_INTERVAL)
        job.start()
        print("Timer: job called at ", datetime.now(), 'with task interval 24 hours (', TASK_DELAY_INTERVAL_24_HOURS,
              ') seconds.\n')
    while True:
        try:
            time.sleep(SLEEP_INTERVAL)
        except ProgramKilled:
            print("Program killed: stopping tasks at ", datetime.now(), '.\n')
            job.stop()
            break


#run_task(TASK_DELAY_INTERVAL_10_MINUTES, run_scheduled_jobs)
