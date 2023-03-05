import time

def get_unix_timestamp():
    """Returns the current Unix timestamp in milliseconds."""
    return int(time.time() * 1000)
