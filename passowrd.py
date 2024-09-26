import string
from random import choice, randint, shuffle
class Password:
    def __init__(self):
        self.letters = string.ascii_letters
        self.numbers  = string.digits
        self.symbols = ["@", "!", ".", "$", "#", "&", "*", "+",]
        self.num_letter = randint(8, 10)
        self.num_numbers = randint(2, 4)
        self.num_symbols = randint(2, 4)

    def generate_password(self)-> str:
        """_Generate a password that includes letters, numbers and symbols_

        Returns:
            str: _generated password_
        """
        password = []
        for _ in range(self.num_letter):
            password.append(choice(self.letters))
        for _ in range(self.num_numbers):
            password.append(choice(self.numbers))
        for _ in range(self.num_symbols):
            password.append(choice(self.symbols))
        shuffle(password)
        return "".join(letter for letter in password)