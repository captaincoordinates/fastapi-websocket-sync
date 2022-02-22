import os

# From the os package docs discussing os.cpu_count()
# https://docs.python.org/3/library/os.html#os.cpu_count
# "This number is not equivalent to the number of CPUs the current process can use.
# The number of usable CPUs can be obtained with len(os.sched_getaffinity(0))"
num_avail_cpus = len(os.sched_getaffinity(0))

loglevel = os.environ.get("API_LOG_LEVEL", "INFO")
worker_class = "uvicorn.workers.UvicornWorker"
workers = num_avail_cpus
bind = "0.0.0.0:80"
