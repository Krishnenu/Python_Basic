from functools import wraps
from time import time


def retry(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        for attempt in range(1, 4):
            try:
                return fn(*args, **kwargs)
            except Exception as e:
                print(f"⚠️ Attempt {attempt} failed: {e}")
                if attempt == 3:
                    raise Exception("Retry limit reached")
    return wrapper


@retry
def retryLogic(promt):
    print(promt)
    raise ConnectionError("Server unavailable")

retryLogic("hellow")
retryLogic("hellow")
retryLogic("hellow")

# retryLogic("hellow")
# retryLogic("hellow")
# retryLogic("hellow")


# this is decorator code

