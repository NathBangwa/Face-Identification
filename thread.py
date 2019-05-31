from tkinter import *
import time
from threading import Thread, RLock

lock = RLock()
class UI:
    def __init__(self):
        self.root = Tk()
    
    async def start(self):
        self.root.mainloop()


class Logical:
    def __init__(self):
        pass
    
    async def start(self):
        while True:
            with lock:
                print("hello")
                time.sleep(1)


import asyncio
async def main():
    print(await 7 * 7)
#help(asyncio)
ui = UI()
log = Logical()
loop = asyncio.get_event_loop()
loop.create_task(ui.start())
loop.create_task(log.start())

loop.run(main())
