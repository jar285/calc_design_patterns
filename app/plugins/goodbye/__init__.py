import logging
from app.commands import Command

class GoodbyeCommand(Command):
    def execute(self):
        # Log the goodbye message instead of printing it
        logging.info("Goodbye")