from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk

class ButtonFrame(tk.Frame):
    def __init__(self, window):
        super().__init__(window)
        self.window = window
    
        # frame set up
        self.rowconfigure((0,1,2,3,4,5), weight=1, uniform='a')
        self.columnconfigure((0,1), weight=1, uniform='a')

        # create frame widgets
        self.create_widgets()

    def create_widgets(self):
        # color buttons
        self.black_button = tk.Button(self, background='black', command=lambda: self.window.set_color('black'))
        self.red_button = tk.Button(self, background='red', command=lambda: self.window.set_color('red'))
        self.blue_button = tk.Button(self, background='blue', command=lambda: self.window.set_color('blue'))
        self.green_button = tk.Button(self, background='green', command=lambda: self.window.set_color('green'))
        self.yellow_button = tk.Button(self, background='yellow', command=lambda: self.window.set_color('yellow'))

        # tool buttons
        self.eraser_image = ImageTk.PhotoImage((Image.open('images/eraser.png')).resize((120,120)))
        self.clear_image = ImageTk.PhotoImage((Image.open('images/clear.png')).resize((120,120)))
        self.fill_image = ImageTk.PhotoImage((Image.open('images/fill.png')).resize((120,120)))
        self.eraser_button = ttk.Button(self, image=self.eraser_image)
        self.clear_button = ttk.Button(self, image=self.clear_image)
        self.fill_button = ttk.Button(self, image=self.fill_image)

        # place
        self.black_button.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
        self.red_button.grid(row=4, column=0, sticky='nsew', padx=10, pady=10)
        self.blue_button.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)
        self.green_button.grid(row=3, column=0, sticky='nsew', padx=10, pady=10)
        self.yellow_button.grid(row=2, column=0, sticky='nsew', padx=10, pady=10)
        self.eraser_button.grid(row=0, column=1, sticky='nsew', padx=10, pady=10)
        self.clear_button.grid(row=2, column=1, sticky='nsew', padx=10, pady=10)
        self.fill_button.grid(row=1, column=1, sticky='nsew', padx=10, pady=10)


class CanvasFrame(tk.Frame):
    def __init__(self, window):
        super().__init__(window, bg='white')
        self.window = window

        # create frame widgets  
        self.create_widgets()

    def create_widgets(self):
        # main canvas
        self.canvas = tk.Canvas(self, background='white')
        self.canvas.pack(expand=True, fill='both')
        self.canvas.bind()
        self.canvas.bind('<B1-Motion>', self.draw)
        self.canvas.bind('<Button-1>', self.draw)
    
    def draw(self, event):
        self.canvas.create_oval((event.x, event.y, event.x, event.y), 
                                fill=self.window.get_color() , 
                                width=self.window.current_brush_size
                                )

class SliderFrame(tk.Frame):
    def __init__(self, window):
        super().__init__(window, bg='white')