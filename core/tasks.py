import multiprocessing as mp
from multiprocessing import Pool
#http://gouthamanbalaraman.com/blog/python-multiprocessing-as-a-task-queue.html

pool = Pool(processes=4)
jobs = {}
running = {}
executed = {}
errors = {}

def some_job():
    return "Job done!"