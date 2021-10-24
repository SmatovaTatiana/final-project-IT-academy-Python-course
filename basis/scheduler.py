import datetime
import sched
import time
from basis.mailing import send_email
from basis.scrapper import run_scrapper
from datetime import datetime


s = sched.scheduler(time.time, time.sleep)

DELAY = 10
NO_DELAY = 0
HIGH_PRIORITY = 1
LOW_PRIORITY = 2


def run_scheduled_jobs():
    s.enter(NO_DELAY, HIGH_PRIORITY, run_scrapper)
    s.enter(DELAY, LOW_PRIORITY, send_email)
    print("Scheduler run jobs started at ", datetime.now(), '.\n')
    s.run()
    print("Scheduler run jobs finished at ", datetime.now(), '.\n')


# run_scheduled_jobs()
