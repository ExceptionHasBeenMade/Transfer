from multiprocessing import Process
from time import sleep
import json

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
        try:
            with open("./connect.json", encoding='utf-8', errors='ignore') as json_data:
                imported = json.load(json_data, strict=False)
        except json.decoder.JSONDecodeError:
            pass
        if (imported["action"]):
            print("Read")
            sleep(0.0002)
            pass

if __name__ == '__main__':
    q = Process(target=clock)
    s = Process(target=check)
    q.start()
    s.start()
    q.join()
    s.join()
