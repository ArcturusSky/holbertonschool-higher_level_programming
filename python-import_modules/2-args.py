#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = len(sys.argv) - 1
    
    if args == 0:
        print("0 arguments.")
    
    elif args == 1:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))

    else:
        index = 1
        print("{} arguments:".format(args))
        while index <= args:
            print("{}: {}".format(index, sys.argv[index]))
