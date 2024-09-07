#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = len(sys.argv) - 1
    
    if args == 0:
        print("{} argument.".format(args))
    
    elif args == 1:
        print("{} argument:".format(args))
        print("1: {}".format(sys.argv[1]))

    else:
        index = 1
        print("{} arguments:".format(args))
        while index <= args:
            print("{}: {}".format(index, sys.argv[index]))
