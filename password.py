import string
from random import choice, randint, shuffle
class Password:
    def __init__(self, password_field):
        self.letters = string.ascii_letters
        self.numbers  = string.digits
        self.symbols = ["@", "!", "$", "#", "&", "*", "+",]
        self.num_letters = randint(8, 10)
        self.num_numbers = randint(2, 4)
        self.num_symbols = randint(2, 4)
        self.password = ""
        self.password_field = password_field

    def generate_password(self)-> str:
        """_Generate a password that includes letters, numbers and symbols_

        Returns:
            str: _generated password_
        """
        self.password_field.delete(0, 'end')
        password_1 = [choice(self.letters) for _ in range(self.num_letters)]
        password_1 += [choice(self.numbers) for _ in range(self.num_numbers)]
        password_1 += [choice(self.symbols) for _ in range(self.num_symbols)]

        shuffle(password_1)
        self.password= "".join(password_1)
        self.password_field.insert(0, self.password)

