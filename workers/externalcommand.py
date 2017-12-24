#!/usr/bin/env python3

import os
import subprocess as sp


debugon = False
forks = 3
worklist = ["127.0.0.1", "localhost", "128.10.10.1"]


def worker(var):

    FNULL = open(os.devnull, 'w')

    r = sp.call(["ping", "-c 1", "-W 2", var], stdout=FNULL, stderr=sp.STDOUT)
    if r == 0:
        print("Success {}".format(var))
    else:
        print("Failure {}".format(var))

    FNULL.close()

    return(0)


if __name__ == "__main__":

    worker("127.0.0.1")
