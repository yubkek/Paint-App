from tkinter import ttk
import tkinter as tk
from widgets import *
from PIL import Image, ImageTk
import pickle
W = 1200
H = 900

class Paint(tk.Tk):
    def __init__(self):
        # history of canvas
        self.undo_list = []
        self.redo_list = []

        # window set up
        super().__init__()
        self.title('Paint')
        self.geometry(f'{W}x{H}+700+300')
        self.rowconfigure((0,1,2,3,4,5), weight=1, uniform='a')
        self.columnconfigure((0,1,2), weight=1, uniform='a')
        self.resizable(width=False, height=False)

        # paint variables
        self.current_color = 'black'
        self.current_brush_size = tk.IntVar(value=10)
        self.clear = False
        self.fill = False

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
        self.canvas_frame.grid(row=0, column=0, rowspan=4, columnspan=2, sticky='nsew')

        # button frame
        self.button_frame.grid(row=0, column=2, rowspan=5, columnspan=1, sticky='nsew')

        # slider frame
        self.slider_frame.grid(row=4, column=0, columnspan=2, sticky='nsew')

    def set_color(self, color):
        self.current_color = color

    def get_color(self) -> str:
        return self.current_color
    
    def set_brush(self, brush_width):
        self.current_brush_size = brush_width

    def get_brush(self) -> int:
        return self.current_brush_size.get()
    
    def set_clear(self):
        self.clear = not self.clear

    def get_clear(self) -> bool:
        return self.clear
    
    def set_fill(self):
        self.fill = not self.fill

    def get_fill(self) -> bool:
        return self.fill

if __name__ == "__main__":
    paint_app = Paint()