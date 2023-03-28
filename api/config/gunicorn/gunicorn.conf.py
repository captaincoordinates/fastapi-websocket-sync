from logging import getLogger
from os import environ, sched_getaffinity  # type: ignore

logger = getLogger(__file__)

cpu_core_count = len(sched_getaffinity(0))
try:
    cpu_core_limit = min(
        int(environ.get("CPU_CORE_LIMIT", cpu_core_count)), cpu_core_count
    )
    logger.debug(f"cpu_core_limit: {cpu_core_limit}")
    workers_per_core = float(environ.get("WORKERS_PER_CORE", 1))
    logger.debug(f"workers_per_core: {workers_per_core}")
    workers = round(cpu_core_limit * workers_per_core)
except Exception as e:
    workers = cpu_core_count
    logger.error(f"default number of workers ({workers}): {e}")

default_bind_port = 80
try:
    bind_port = int(environ.get("BIND_PORT", default_bind_port))
except Exception:
    logger.error(f"unable to parse BIND_PORT ({environ['BIND_PORT']})")
    bind_port = default_bind_port

bind = f"0.0.0.0:{bind_port}"
worker_class = "uvicorn.workers.UvicornWorker"

logger.info(
    f"gunicorn config workers: {workers}, worker_class: {worker_class}, bind: {bind}"
)
