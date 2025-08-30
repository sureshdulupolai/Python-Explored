# Infinite Loops: Timeouts
# pip install -q pytest-timeout
# pip show pytest-timeout

import time
import pytest

@pytest.mark.timeout(2)  # yeh test max 2 seconds chalega
def test_slow_function():
    while True:
        time.sleep(1)
        print('sleeping...')

def test_empty():
    pass
