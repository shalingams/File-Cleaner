from tkinter import StringVar, Tk, Label, Button, Frame, PhotoImage
from backend import cleaner
from tkinter import filedialog

root = Tk()
root.title("Desktop Cleaner")
root.config(bg="skyblue")
root.minsize(400, 400)  # width, height

left_frame = Frame(root, width=400, height=400)
left_frame.grid(row=0, column=0, padx=10, pady=5)


path = StringVar()

def browse_button():
    filename = filedialog.askdirectory()
    print(filename)
    path.set(filename)
    

left_frame = Frame(root, width=200, height=400, bg="skyblue")
left_frame.grid(row=0, column=0, padx=10, pady=5)

Label(left_frame, text="Select A folder to clean").grid(row=0, column=0, padx=5, pady=5)

image = PhotoImage(file="file_organizer_logo.png")
original_image = image.subsample(3, 3)
Label(left_frame, image=original_image).grid(row=1, column=0, padx=5, pady=5)

tool_bar = Frame(left_frame, width=180, height=185, bg="skyblue")
tool_bar.grid(row=2, column=0, padx=5, pady=5)

Button(tool_bar, text="Browse", command=browse_button).grid(
    row=0, column=0, padx=5, pady=3, ipadx=10
)

Button(tool_bar, text="Clean", command=lambda: cleaner(path.get())).grid(
    row=1, column=0, padx=5, pady=3, ipadx=10
)


root.mainloop()
