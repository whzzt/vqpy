import time

class Profiler:
    # profile the operator performance

    def __init__(self) -> None:
        self.instance_count = 0
        self.total_time = 0.0

    def start(self):
        self.total_time -= time.perf_counter()

    def end(self):
        self.instance_count += 1
        self.total_time += time.perf_counter()
