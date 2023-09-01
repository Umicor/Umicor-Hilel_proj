import time
import logging


class TimerContext:
    def __enter__(self):
        print("Start")
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # logger.info(...)
        print("Stop")
        self.end = time.time()
        self.res = self.end - self.start
        return False


# Set up logging configuration
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

with TimerContext() as timer:
    time.sleep(2)

print("Timer: " + str(timer.res))
