import time 
import threading
from multiprocessing import Process 

# normal function
def task(name=None):
    start_time = time.time()
    print(f"Task '{name}' started")
    time.sleep(2)  # Simulate a task taking some time
    print(f"Task '{name}' completed in {time.time() - start_time} seconds")
# task("Example Task")

# threading example
def thread_task(name=None):
    start_time = time.time()
    print(f"Thread Task '{name}' started")
    time.sleep(2)  # Simulate a task taking some time
    print(f"Thread Task '{name}' completed in {time.time() - start_time} seconds")

t1 = threading.Thread(target=task, args=("Thread 1",))
t2 = threading.Thread(target=thread_task, args=("Thread 2",))

t1.start()
t2.start()

t1.join()
t2.join()

print("All threads completed")


# process example
def process_task():
    start_time = time.time()
    print(f"Process Task started")
    time.sleep(2)  # Simulate a task taking some time
    print(f"Process Task completed in {time.time() - start_time} seconds")


p1 = Process(target=process_task)
p2 = Process(target=process_task)

# p1.start()
# p2.start()

# p1.join()
# p2.join()

# print("All processes completed")
