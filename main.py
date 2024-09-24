from tkinter import Tk, Label, Button, Canvas, PhotoImage
def main()->None:
    window = Tk()
    canvas = Canvas(window)
    logo = PhotoImage(file="logo.png")
    canvas.create_image(200, 100, image=logo)
    canvas.grid(row = 1, column = 2)
    window.title("Password Generator")
    window.minsize(400, 100)
    
    window.mainloop()
    
if __name__ == "__main__": 
    main()