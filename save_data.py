class SaveData:
    def __init__(self, website, email, password):
        self.website = website
        self.email = email
        self.password = password
        self.data = {}

    def get_data(self)->None:
        """_Process data from Tkinter Entry field and save them into the data dictionary_
        """
        self.data['website'] = self.website.get()
        self.data['email'] = self.email.get()
        self.data['password'] = self.password.get()

    def save_data_file(self)->None:
        """_Write the website, email and password to data text file_
        """
        with open("data.txt", "a") as file:
                file.write(f"Website: {self.data['website']} | Email: {self.data['email']} | Password: {self.get_data()['password']}\n")
        self.clear_data()
    def clear_data(self):
        self.website.delete(0, 'end')
        self.password.delete(0, 'end')