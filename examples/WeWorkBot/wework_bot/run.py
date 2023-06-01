import sys
import time

import ntwork


def forever():
    try:
        while True:
            time.sleep(0.5)
    except KeyboardInterrupt:
        ntwork.exit_()
        sys.exit()
