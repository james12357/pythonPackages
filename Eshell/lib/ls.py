import os
import sys
print(" ".join(os.listdir(sys.argv[1] if len(sys.argv) > 1 else os.getcwd())))

