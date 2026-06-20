'''Task 2: Random Password Generator
Objective

Use built-in modules.

Requirements

Use:

import random
import string'''

from random import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

