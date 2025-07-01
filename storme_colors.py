import random

# Cores ANSI personalizadas
class Colors:
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    PURPLE = "\033[35m"
    CYAN = "\033[36m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

def random_color():
    return random.choice([
        Colors.RED, Colors.GREEN, Colors.YELLOW, 
        Colors.BLUE, Colors.PURPLE, Colors.CYAN
    ])