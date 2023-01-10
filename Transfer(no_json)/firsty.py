from multiprocessing import Process
from time import sleep

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
        from secondy import callback
        if(callback):
            print("Readed")
            sleep(1)
            del callback

if __name__ == '__main__':
    q = Process(target=clock)
    s = Process(target=check)
    q.start()
    s.start()
    q.join()
    s.join()
