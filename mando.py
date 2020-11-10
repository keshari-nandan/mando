import os
import sys
from utilities.commands import *

args = sys.argv

if args[1] == INIT:
    cwd = os.getcwd() + '/' + args[0]
    print(cwd)
else:
    print('Unknown')