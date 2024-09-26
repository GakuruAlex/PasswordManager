import string
from random import choice, randint, shuffle
class Password:
    def __init__(self):
        self.letters = string.ascii_letters
        self.numbers  = string.digits
        self.symbols = ["@", "!", "$", "#", "&", "*", "+",]
        self.num_letters = randint(8, 10)
        self.num_numbers = randint(2, 4)
        self.num_symbols = randint(2, 4)

    def generate_password(self)-> str:
        """_Generate a password that includes letters, numbers and symbols_

        Returns:
            str: _generated password_
        """
        password = [choice(self.letters) for _ in range(self.num_letters)]
        password += [choice(self.numbers) for _ in range(self.num_numbers)]
        password += [choice(self.symbols) for _ in range(self.num_symbols)]

        shuffle(password)
        return "".join(letter for letter in password)
