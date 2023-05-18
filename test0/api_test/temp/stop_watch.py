import time
import sys

start_time = time.time()

while True:
    current_time = time.time()
    elapsed_time = current_time - start_time
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    milliseconds = int((elapsed_time - seconds) * 1000)
    sys.stdout.write(f"\r{minutes:02d}:{seconds:02d}:{milliseconds:03d}")
    sys.stdout.flush()
    time.sleep(0.01)
