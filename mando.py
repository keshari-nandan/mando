import os
import sys
from setup.alias import create_alias

from utilities.commands import *

args = sys.argv

if len(args) > 1 and args[1] == INIT:
    create_alias(args)
else:
    print('Unknown')