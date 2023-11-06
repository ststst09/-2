
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Scrollbar


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\user\Desktop\체질 파이썬 파일(완성본)\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1025x1100")
window.configure(bg = "#FFFFFF")

window.title("체질 파이썬 파일")
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1000,
    width = 912,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    456.0,
    68.99999999999994,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    512.0,
    892.0,
    image=image_image_2
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat",
)
button_1.place(
    x=280.0,
    y=1000.0,
    width=466.0,
    height=72.0
)

button_window = canvas.create_window(
    513.0,
    1380.0,
    window=button_1,
    width=466.0,
    height=72.0
)




image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    68.0,
    265.00000000000006,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    282.0,
    195.00000000000006,
    image=image_image_4
)

# 스크롤
def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

def on_mousewheel(event):
    canvas.yview_scroll(-1 * (event.delta // 120), "units")



canvas.pack(fill="both", expand=True)
scrollbar = Scrollbar(window, orient="vertical", command=canvas.yview)

# Place the Canvas and Scrollbar
canvas.place(x=0, y=0)
scrollbar.pack(side="right", fill="y")

canvas.configure(yscrollcommand=scrollbar.set)

canvas.bind('<Configure>', on_configure)
canvas.bind('<MouseWheel>', on_configure)
canvas.bind_all("<MouseWheel>", on_mousewheel)

window.resizable(False, False)
window.mainloop()
