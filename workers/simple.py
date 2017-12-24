#!/usr/bin/env python3

debugon = False
forks = 3
worklist = ["Hello World", "Hello Moon", "Hello Mars", "Hello Sun"]


def worker(var):

    print(var)
    return(0)


if __name__ == "__main__":

    worker("Hello World")
