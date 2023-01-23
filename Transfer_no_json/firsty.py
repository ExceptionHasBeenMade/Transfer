from threading import Thread, Event
# import threading
from time import sleep
# from secondy import option
# import ctypes

def clock():
    hours = 0
    minutes = 0
    seconds = 0
    while True:
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        seconds += 1
        sleep(1)
        if seconds == 60:
            seconds = 0
            minutes += 1
        if minutes == 60:
            minutes = 0
            hours += 1
        if hours == 24:
            hours = 0

def check():
    while True:
        if(callback.wait()):
            print("Read")
            del callback

if __name__ == '__main__':
    q = Thread(target=clock)
    s = Thread(target=check)
    q.start()
    s.start()
    q.join()
    s.join()
# example of using an event object
# from time import sleep
# from random import random
# from threading import Thread
# from threading import Event

# # target task function
# def task(event, number):
#     # wait for the event to be set
#     event.wait()
#     # begin processing
#     value = random()
#     sleep(value)
#     print(f'Thread {number} got {value}')

# # create a shared event object
# event = Event()
# # create a suite of threads
# for i in range(5):
#     thread = Thread(target=task, args=(event, i))
#     thread.start()
# # block for a moment
# print('Main thread blocking...')
# sleep(2)
# # start processing in all threads
# event.set()
# # wait for all the threads to finish...