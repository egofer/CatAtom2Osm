import sys
from io import TextIOWrapper, BytesIO
from contextlib import contextmanager

@contextmanager
def capture(command, *args, **kwargs):
    out = sys.stdout
    sys.stdout = TextIOWrapper(BytesIO(), 'utf-8')
    try:
        command(*args, **kwargs)
        sys.stdout.seek(0)
        yield sys.stdout.read()
    finally:
        sys.stdout = out


