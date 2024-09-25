from tkinter import Tk, Label, Button, Canvas, PhotoImage,  Entry, StringVar
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
    email = StringVar(value=EMAIL)
    window.title("Password Generator")
    #Pad window
    window.config(padx=20, pady=20)
    canvas = Canvas(window, width=200, height=200,)
    #Load logo
    logo = PhotoImage(file="logo.png")
    #Create image on the canvas
    canvas.create_image(100, 100, image=logo)
    canvas.grid(row=0, column=1, padx=0, pady=20, )

    # Website label
    website_text = Label(window, text="Website:", font=FONT, )
    website_text.grid(row=1, column=0, pady=PADY)

    # Input field for website name
    website_input = Entry(window, width=FULL_WIDTH)
    website_input.grid(row=1, column = 1, columnspan=2, pady=PADY)

    #Email/username label
    email_label = Label(window, text="Email/Username:", font=FONT)
    email_label.grid(row=2, column=0, pady=PADY)

    #Email/Username
    email_field =  Entry(window, textvariable= email, width= FULL_WIDTH , font= FONT)
    email_field.grid(row= 2, column= 1,  columnspan= 2, pady=PADY)

    #Password Label
    password_label = Label(window, text="Password:",font=FONT, )
    password_label.grid(row = 3, column=0, pady= PADY)

    #Password Entry
    password_field = Entry(window, width= PASSWORD_INPUT_WIDTH)
    password_field.grid(row= 3, column=1, pady=PADY)

    #Generate password button
    password_button = Button(window, text="Generate Password", font=PASSWORD_FONT ,width=PASSWORD_BUTTON_WIDTH)
    password_button.grid(row= 3, column=2, pady= PADY)

    #Button for saving content
    add_button = Button(window, text="Add", font=PASSWORD_FONT, width= ADD_BUTTON_WIDTH)
    add_button.grid(row= 4, column=1, columnspan= 2)



    # Start main loop
    window.mainloop()

if __name__ == "__main__": 
    main()