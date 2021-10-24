'''
https://docs.python.org/3/library/sched.html
scheduler.enter(delay, priority, action, argument=(), kwargs={})
Schedule a new event. The time argument should be a numeric type compatible with the return value
of the timefunc function passed to the constructor. Events scheduled for the same time will be executed in the order
of their priority. A lower number represents a higher priority.
Executing the event means executing action(*argument, **kwargs).
argument is a sequence holding the positional arguments for action.
kwargs is a dictionary holding the keyword arguments for action.
Return value is an event which may be used for later cancellation of the event (see cancel()).
'''

import datetime
import sched
import time
from datetime import datetime

from basis.mailing import send_email
from basis.scrapper import run_scrapper

s = sched.scheduler(time.time, time.sleep)

DELAY = 10   # seconds
NO_DELAY = 0
HIGH_PRIORITY = 1
LOW_PRIORITY = 2


def run_scheduled_jobs():
    s.enter(NO_DELAY, HIGH_PRIORITY, run_scrapper)
    s.enter(DELAY, LOW_PRIORITY, send_email)
    print("Scheduler run jobs started at ", datetime.now(), '.\n')
    s.run()
    print("Scheduler run jobs finished at ", datetime.now(), '.\n')


#run_scheduled_jobs()
