#!/usr/bin/python3
import sys

if __name__ == "__main__":

    args = len(sys.argv) - 1

    if args == 0:
        print("0 argument.")

    elif args == 1:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))

    else:
        print("{} arguments:".format(args))
        for index in range(1, args + 1):
            print("{}: {}".format(index, sys.argv[index]))
