import sys
from app import Command


class ExitCommand(Command):
    def execute(self):
        sys.exit("Exiting...")