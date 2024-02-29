import sys
from app.commands import Command


class DiscordCommand(Command):
    def execute(self):
        print(f'I just sent something to discord')