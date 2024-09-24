from tkinter import Tk, Label, Button, Canvas, PhotoImage
def main()->None:
    window = Tk()
    canvas = Canvas(window, width=200, height=200, bg="green",)
    
    logo = PhotoImage(file="logo.png")
    canvas.create_image(100, 100, image=logo)
    
    canvas.grid(padx=20, pady=20, )

    window.title("Password Generator")

    
    window.mainloop()
    
if __name__ == "__main__": 
    main()