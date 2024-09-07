#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arg_count = len(sys.argv) - 1
    addresult = 0

    for index in range(1, arg_count + 1):
        addresult += int(sys.argv[index])

    print(addresult)
