#!/usr/bin/env python3

debugon = 0
forks = 1
worklist = ["Hello World"]


def worker(var):

    print(var)
    return(0)


if __name__ == "__main__":

    worker("Hello World")
