from tkinter import ttk
import tkinter as tk
from widgets import *
W = 1200
H = 900

class Paint:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Paint')
        self.window.geometry(f'{W}x{H}+700+300')
        self.window.rowconfigure((0,1,2,3,4,5), weight=1, uniform='a')
        self.window.columnconfigure((0,1,2), weight=1, uniform='a')

        self.create_widgets()
        self.place_widgets()

    def run(self):
        self.window.mainloop()

    def create_widgets(self):
        # frames
        self.canvas_frame = Frame(self.window)
        self.button_frame = Frame(self.window)
        self.slider_frame = Frame(self.window)

        # canvas
        self.canvas = Canvas(self.canvas_frame.frame)

        # buttons
        self.red_button = Button(self.button_frame.frame)
        self.blue_button = Button(self.button_frame.frame)
        self.green_button = Button(self.button_frame.frame)
        self.orange_button = Button(self.button_frame.frame)
        self.yellow_button = Button(self.button_frame.frame)
        self.eraser_button = Button(self.button_frame.frame)
        self.fill_button = Button(self.button_frame.frame)
        self.clear_button = Button(self.button_frame.frame)

        # slider
        self.thickness_slider = Slider(self.slider_frame.frame)

    def place_widgets(self):
        # canvas frame
        self.canvas_frame.frame.grid(row=0, column=0, rowspan=5, columnspan=2, sticky='nsew')
        self.canvas.canvas.pack(expand=True, fill='both')

        # button frame
        

        # slider frame


if __name__ == "__main__":
    paint_app = Paint()
    paint_app.run()