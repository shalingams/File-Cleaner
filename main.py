from tkinter import StringVar, Tk, Label, Button
from backend import cleaner
from tkinter import filedialog

root = Tk()
root.title("Desktop Cleaner")
root.minsize(800, 400)  # width, height
root.geometry("300x300+50+50")

path = StringVar()

def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    filename = filedialog.askdirectory()
    print(filename)
    path.set(filename)
    
text = Label(root, text="Select A folder to clean")
text.pack()

button2 = Button(text="Browse", command=browse_button)
button2.pack()

clean = Button(root, text="Clean", command=lambda: cleaner(path.get()))
clean.pack()

root.mainloop()
