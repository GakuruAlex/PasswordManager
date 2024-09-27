from tkinter import Tk, Label, Button, Canvas, PhotoImage,  Entry
from save_data import SaveData
from password import Password
FONT = ("Rubik", 10, )
EMAIL = "johndoe@dow.com"
FULL_WIDTH = 45
ADD_BUTTON_WIDTH = 50
PASSWORD_INPUT_WIDTH = 28
PASSWORD_BUTTON_WIDTH = 15
PASSWORD_FONT = ("Rubik", 8, )
PADX = 5
PADY = 5


def main()->None:
    
    #Create a window 
    window = Tk()
    # Title of the app
    
    window.title("Password Manager")
    #Pad window
    window.config(padx=20, pady=20)
    canvas = Canvas(window, width=200, height=200,)
    #Load logo
    logo = PhotoImage(file="/home/aleyg/projects/Python/100DaysOfCode/DayTwentyNine/PasswordManager/logo.png")
    #Create image on the canvas
    canvas.create_image(100, 100, image=logo)
    canvas.grid(row=0, column=1, padx=0, pady=20, )

    # Website label
    website_text = Label(window, text="Website:", font=FONT, )
    website_text.grid(row=1, column=0, pady=PADY)

    # Input field for website name
    website_input = Entry(window, width=PASSWORD_INPUT_WIDTH)
    website_input.grid(row=1, column = 1, pady=PADY)
    website_input.focus()

    #Email/username label
    email_label = Label(window, text="Email/Username:", font=FONT)
    email_label.grid(row=2, column=0, pady=PADY)

    #Email/Username
    email_field =  Entry(window,  width= FULL_WIDTH , font= FONT)
    email_field.grid(row= 2, column= 1,  columnspan= 2, pady=PADY)
    email_field.insert(0, EMAIL)

    #Password Label
    password_label = Label(window, text="Password:",font=FONT, )
    password_label.grid(row = 3, column=0, pady= PADY)

    #Password Entry
    password_field = Entry(window, width= PASSWORD_INPUT_WIDTH)
    password_field.grid(row= 3, column=1, pady=PADY)
    generated_password = Password(password_field=password_field)
    #Generate password button
    password_button = Button(window, text="Generate Password", font=PASSWORD_FONT ,width=PASSWORD_BUTTON_WIDTH, command=generated_password.generate_password)
    password_button.grid(row= 3, column=2, pady= PADY)

    # Create a SaveData object and instantiate with the entry fields
    save_data = SaveData(website_input, email_field, password_field)

    #Button for saving content
    add_button = Button(window, text="Add", font=PASSWORD_FONT, width= ADD_BUTTON_WIDTH, command=save_data.save_data_file)
    add_button.grid(row= 4, column=1, columnspan= 2)

     # Search button
    search = Button(text="Search", width=PASSWORD_BUTTON_WIDTH, font=PASSWORD_FONT, command=save_data.search)
    search.grid(row=1, column= 2)


    # Start main loop
    window.mainloop()

if __name__ == "__main__":
    main()