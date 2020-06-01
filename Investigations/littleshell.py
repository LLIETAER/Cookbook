#!/usr/bin/env python
"""
(Python >= 3.6)
This is an example of how to prompt inside an application that uses the asyncio
eventloop. The ``prompt_toolkit`` library will make sure that when other
coroutines are writing to stdout, they write above the prompt, not destroying
the input line.
This example does several things:
    1. It starts a simple coroutine, printing a counter to stdout every second.
    2. It starts a simple input/echo app loop which reads from stdin.
Very important is the following patch. If you are pashsing stdin by reference to
other parts of the code, make sure that this patch is applied as early as
possible. ::
    sys.stdout = app.stdout_proxy()
"""

import asyncio
import time

from prompt_toolkit.patch_stdout import patch_stdout
from prompt_toolkit.shortcuts import PromptSession


async def print_counter():
    """
    Coroutine that prints counters.
    """
    try:
        for i in range(10):
            print("Counter: %i" % i)
            i += 1
            await asyncio.sleep(3)
    except asyncio.CancelledError:
        print("Background task cancelled.")


async def interactive_shell():
    """
    Like `interactive_shell`, but doing things manual.
    """
    # Create Prompt.
    def get_toolbar():
        return "Bottom toolbar: time=%r" % time.time()

    session = PromptSession("Say something: ")

    # Run echo loop. Read text from stdin, and reply it back.
    while True:
        try:
            result = await session.prompt_async(">:",
                                                bottom_toolbar=get_toolbar,
                                                refresh_interval=0.5)
            print('You said: "{0}"'.format(result))
            if result == 'start':
                background_task = asyncio.create_task(print_counter())
            for task in asyncio.all_tasks():
                print(task)
        except (EOFError, KeyboardInterrupt):
            print("key")
            return


async def main():
    with patch_stdout():
        #background_task = asyncio.create_task(print_counter())
        #try:
        await interactive_shell()
        #finally:
            #background_task.cancel()
        #print("Quitting event loop. Bye.")


if __name__ == "__main__":
    try:
        from asyncio import run
    except ImportError:
        asyncio.run_until_complete(main())
    else:
        asyncio.run(main())

