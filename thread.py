from tkinter import *
import time
from threading import Thread, RLock

lock = RLock()
class UI:
    def __init__(self):
        self.root = Tk()
        self.root.mainloop()


class Logical:
    def __init__(self):
        pass
    
    def start(self):
        while True:
            with lock:
                print("hello")
                time.sleep(1)


import asyncio
async def main():
    print(await 7 * 7)
#help(asyncio)
ui = UI
log = Logical()
t1 = Thread(target=log.start)
t2 = Thread(target=ui)

t1.start()
t2.start()

t1.join()
t2.join()
"""
loop = asyncio.get_event_loop()
loop.create_task(ui.start())
loop.create_task(log.start())
"""
#loop.run(main())
