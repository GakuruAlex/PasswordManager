from tkinter import messagebox
from json import dump, load, JSONDecodeError
class SaveData:
    def __init__(self, website, email, password):
        self.website = website
        self.email = email
        self.password = password
        self.data = {}

    def get_data(self)->None:
        """_Process data from Tkinter Entry field and save them into the data dictionary_
        """
        self.entered_website = self.website.get()
        self.data[self.entered_website] = {"email":self.email.get(),"password": self.password.get()}

    def save_data_file(self)->None:
        """_Write the website, email and password to data text file_
        """
        self.get_data()
        if self.is_website_or_password_empty():
            messagebox.showerror(title="Missing Fields", message="Website and Password cannot be empty")
        else:
            if self.is_ready_to_save():
                self.save_data_to_json()
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
        return len(self.entered_website)==0 or len(self.data[self.entered_website]['password']) == 0
    def is_ready_to_save(self)->bool:
        """_Confirm user wishes to save the given info_

        Returns:
            bool: _True for ok or False for cancel_
        """
        return messagebox.askokcancel(title="Save", message=f"Are you sure you want to save\n Website: {self.entered_website} \n Password: {self.data[self.entered_website]['password']}")
    def save_data_to_json(self)-> None:
        """_Read json file contents if it exist, update with new data and then save or create a new 
        json file and save to it_
        """
        try:
            with open("data.json","r") as file:
                old_data = load(file)

            with open("data.json", "w") as file:
                old_data.update(self.data)
                dump(old_data, file ,indent=4)
        except (FileNotFoundError, JSONDecodeError):
            with open("data.json", "w") as file:
                dump(self.data, file, indent=4)
        finally:
                self.clear_data()

  
