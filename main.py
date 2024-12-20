from tkinter import ttk
import tkinter as tk
from widgets import *
from PIL import Image, ImageTk
W = 1200
H = 900

class Paint(tk.Tk):
    def __init__(self):
        # window set up
        super().__init__()
        self.title('Paint')
        self.geometry(f'{W}x{H}+700+300')
        self.rowconfigure((0,1,2,3,4,5), weight=1, uniform='a')
        self.columnconfigure((0,1,2), weight=1, uniform='a')
        self.resizable(width=False, height=False)

        # paint variables
        self.current_color = 'black'
        self.current_brush_size = 3

        # create widgets 
        self.create_widgets()
        self.place_widgets()

        # run
        self.mainloop()
        
    def create_widgets(self):
        # frames
        self.canvas_frame = CanvasFrame(self)
        self.button_frame = ButtonFrame(self)
        self.slider_frame = SliderFrame(self)

    def place_widgets(self):
        # canvas frame
        self.canvas_frame.grid(row=0, column=0, rowspan=5, columnspan=2, sticky='nsew')

        # button frame
        self.button_frame.grid(row=0, column=2, rowspan=5, columnspan=1, sticky='nsew')

        # slider frame
        self.slider_frame.grid(row=5, column=0, columnspan=2, sticky='nsew')

    def set_color(self, color):
        self.current_color = color
        print(self.current_color)

    def get_color(self) -> str:
        print(self.current_color)
        return self.current_color

if __name__ == "__main__":
    paint_app = Paint()