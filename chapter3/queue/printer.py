import random
from queue_ import Queue_


class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def get_stamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):
        return current_time - self.timestamp


class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task is not None:
            self.time_remaining -= 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        if self.current_task is not None:
            return True
        else:
            return False

    def start_next(self, newtask):
        self.current_task = newtask
        self.time_remaining = newtask.get_pages() * 60 / self.pagerate


def new_print_task():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False


def simulation(num_seconds, page_per_minute):
    labprinter = Printer(page_per_minute)
    print_q = Queue_()
    waitingtimes = []
    for current_second in range(num_seconds):
        if new_print_task():
            task = Task(current_second)
            print_q.enqueue(task)
        if (not labprinter.busy()) and (not print_q.is_empty()):
            next_task = print_q.dequeue()
            waitingtimes.append(next_task.wait_time(current_second))
            labprinter.start_next(next_task)
        labprinter.tick()
    average_wait = sum(waitingtimes) / len(waitingtimes)
    print(f'Average Wait {average_wait:6.2f} secs {print_q.size():d} tasks remaining.')


if __name__ == '__main__':
    for i in range(10):
        simulation(3600, 5)
