#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    output = 0
    for i in range(1, len(sys.argv)):
        output += int(sys.argv[i])
    print("{}".format(output))
