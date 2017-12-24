#!/usr/bin/env python3

import socket

#debugon = False
#forks = 3
worklist = ["localhost", "127.0.0.1"]


def worker(var):

    sock = None
    ports = [21, 22, 25, 80, 110, 443, 445, 3306]

    # for port in range(1, 65536):
    for port in ports:

        try:
            sock = socket.create_connection((var, port), 5)
            print("{} - {} - OPEN".format(var, port))
        except ConnectionRefusedError:
            print("{} - {} - ERRConnRefused".format(var, port))
        except socket.timeout:
            print("{} - {} - ERRConnTimeout".format(var, port))

        if sock:
            sock.close()

    return(0)


if __name__ == "__main__":

    worker("127.0.0.1")
