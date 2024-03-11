import logging
import random
from app.commands import Command

class GenerateLuckyNumbersCommand(Command):
    def execute(self):
        lucky_numbers = [random.randint(1, 100) for _ in range(3)]
        logging.info(f"Your lucky numbers are: {lucky_numbers}")
