# app/plugins/generate_lucky_numbers.py

from app.commands import Command
import random

class GenerateLuckyNumbersCommand(Command):
    def execute(self):
        lucky_numbers = [random.randint(1, 100) for _ in range(3)]
        print(f"Your lucky numbers are: {lucky_numbers}")