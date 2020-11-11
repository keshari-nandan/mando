import sys
import click
from setup.setup import create_alias, create_project

from utilities.commands import *

args = sys.argv

if len(args) > 1 and args[1] == INIT:
    create_alias(args)
elif len(args) > 1 and args[1] == START_APP:
    create_project(args)

else:
    args.pop(0)
    click.secho('Unknown command: mando {0}'.format(' '.join(args)), fg='red')
