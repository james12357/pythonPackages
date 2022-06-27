import sys
import getopt
c = -1
opts, args = getopt.getopt(sys.argv[1:], "-c:", ["count="])
for n, v in opts:
    if n in ("-c", "--count"):
        if int(v) < 0:
            raise IOError("Count must be greater than 0.")
        else:
            c = int(v)
if c != -1:
    for i in range(c):
        sys.stdout.write("0")
else:
    while True:
        sys.stdout.write("0")
