class SaveData:
    def __init__(self, website, email, password):
        self.website = website
        self.email = email
        self.password = password

    def get_data(self)->dict:
        """_Process data from Tkinter Entry field_

        Returns:
            dict: _A dictionary of the website, email and password as entered by user_
        """
        website_data = self.website.get()
        email_data = self.email.get()
        password_data = self.password.get()

        return {"website" :website_data, "email":email_data, "password":password_data}

    def save_data_file(self)->None:
        """_Write the website, email and password to data text file_
        """
        with open("data.txt", "a") as file:
                file.write(f"Website: {self.get_data()['website']} | Email: {self.get_data()['email']} | Password: {self.get_data()['password']}\n")
        self.clear_data()
    def clear_data(self):
        self.website.delete(0, 'end')
        self.password.delete(0, 'end')