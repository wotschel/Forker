#!/usr/bin/env python3

import os
import sys

#import workers.portscanner as worker
# import workers.simple as worker
# import workers.template as worker
import workers.externalcommand as worker

def forker():
    global worklist
    # Check if some work has to be done
    try:
        var = worklist.pop()
    except IndexError:
        debug("Nothing left todo!")
        return(5)

    debug(worklist)
    pid = os.fork()

    # Child - Do the work
    if pid == 0:
        result = worker.worker(var)
        os._exit(0)
    else:
        return(pid)


def debug(message):
    global debugon
    if debugon == 1:
        print(message)


def main():
    global work_done

    # Initial Forks
    for i in range(0, forks):
        pid = forker()
        if pid > 0:
            childrens.append(pid)

    debug(childrens)

    while True:
        debug(childrens)
        c = os.wait()
        childrens.remove(c[0])
        debug(c)

        # Define when the work is done
        if len(worklist) == 0:
            work_done = 1

        # Fork new processes if there is work todo
        if work_done == 0:
            pid = forker()
            if pid > 0:
                childrens.append(pid)

        debug(childrens)
        if len(childrens) == 0:
            break


if __name__ == "__main__":

    if "worker" in dir(worker):
        pass
    else:
        sys.stderr.write("\nERR: No worker function present!\n\n")
        exit(-1)

    debugon = worker.debugon
    forks = worker.forks
    worklist = worker.worklist

    debug(worklist)

    childrens = []
    work_done = 0

    if forks > len(worklist):
        sys.stderr.write("Hint: forks is > than objects in worklist\n")
    elif forks == 1:
        sys.stderr.write("Hm... forks is 1?\n")
    elif forks == 0:
        sys.stderr.write("Err: forks is 0\n")
        exit(-1)

    main()
