from tkinter import messagebox
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
        self.get_data()
        if self.is_website_or_password_empty():
            messagebox.showerror(title="Missing Fields", message="Website and Password cannot be empty")
        else:
            if self.is_ready_to_save():
                with open("data.txt", "a") as file:
                    file.write(f"Website: {self.data['website']} | Email: {self.data['email']} | Password: {self.data['password']}\n")
                    self.clear_data()
    def clear_data(self)->None:
        """_Clear the content of the input fields_
        """
        self.website.delete(0, 'end')
        self.password.delete(0, 'end')
    def is_website_or_password_empty(self)-> bool:
        """_Check whether password and website are empty_

        Returns:
            bool: _True if website or password is empty otherwise False_
        """
        return len(self.data['website'])==0 or len(self.data['password']) == 0
    def is_ready_to_save(self)->bool:
        return messagebox.askokcancel(title="Save", message=f"Are you sure you want to save\n Website: {self.data['website']} \n Password: {self.data['password']}")
