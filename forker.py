#!/usr/bin/env python3

import os
import sys
import argparse
import importlib


def forker():
    global worklist
    # Check if some work has to be done
    try:
        var = worklist.pop()
    except IndexError:
        debug("Nothing left todo!")
        return(-5)

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
    if debugon:
        print(message)


def main():
    global work_done

    # Initial Forks
    for i in range(0, forks):
        pid = forker()
        if pid > 0:
            childrens.append(pid)
        if pid == -5:
            debug("Not forking child")

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

    # import workers.simple as worker

    p = argparse.ArgumentParser(description="Forker Script")
    p.add_argument("-f", "--forks", metavar='int', default=2, help="Number of processes to spawn")
    p.add_argument("-d", "--debug", default=False, action="store_true", help="Debug Mode on/off")

    p.add_argument("script")
    args = p.parse_args()

    script = args.script
    if not os.path.exists(script):
        print("Script {} does not exist or is not importable.\n".format(script))
        p.print_help()
        sys.exit(-1)
    else:
        s = script.replace("/", ".")
        s = s.replace(".py", "")

    worker = importlib.import_module(s)

    if args.forks:
        forks = int(args.forks)
    else:
        try:
            forks = int(worker.forks)
        except AttributeError:
            forks = 1

    if args.debug:
        debugon = int(args.debug)
    else:
        try:
            debugon = int(worker.debugon)
        except AttributeError:
            debugon = False

    if "worker" in dir(worker):
        pass
    else:
        sys.stderr.write("\nERR: No worker function present!\n\n")
        exit(-1)

    try:
        worklist = worker.worklist
    except AttributeError:
        sys.stderr.write("\nERR: No worklist present! \n\n")
        exit(-1)

    debug(worklist)

    childrens = []
    work_done = 0
    len_worklist = len(worklist)

    if forks > len_worklist:
        # forks = len_worklist-1
        sys.stderr.write("\nHint: forks is > than objects in worklist\n")
    elif forks == 1:
        sys.stderr.write("Hm... forks is 1?\n")
    elif forks == 0:
        sys.stderr.write("Err: forks is 0\n")
        exit(-1)

    print("Starting Script: {} with {} forks\n".format(script, forks))

    main()
