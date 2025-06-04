import time
from contextlib import contextmanager


@contextmanager
def timer(label: str):
    start = time.time()
    yield
    duration = time.time() - start
    print(f"{label} took {duration:.2f}s")
