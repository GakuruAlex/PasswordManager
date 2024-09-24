from tkinter import Tk, Label, Button, Canvas, PhotoImage
def main()->None:
    #Create a window 
    window = Tk()
    # Title of the app
    window.title("Password Generator")
    canvas = Canvas(window, width=200, height=200, bg="green",)
    #Load logo
    logo = PhotoImage(file="logo.png")
    #Create image on the canvas
    canvas.create_image(100, 100, image=logo)
    canvas.grid(padx=20, pady=20, )

    # Start main loop
    window.mainloop()

if __name__ == "__main__": 
    main()