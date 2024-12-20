from tkinter import ttk
import tkinter as tk

class ButtonFrame(tk.Frame):
    def __init__(self, window):
        super().__init__(window)
    
        # frame set up
        self.rowconfigure((0,1,2,3,4,5), weight=1, uniform='a')
        self.columnconfigure((0,1), weight=1, uniform='a')

        # create frame widgets
        self.create_widgets()

    def create_widgets(self):
        # color buttons
        self.black_button = tk.Button(self, background='black')
        self.red_button = tk.Button(self, background='red')
        self.blue_button = tk.Button(self, background='blue')
        self.green_button = tk.Button(self, background='green')
        self.yellow_button = tk.Button(self, background='yellow')

        # tool buttons
        self.eraser_image = tk.PhotoImage(file='images/s.jpg', height=50, width=50)
        self.clear_image = tk.PhotoImage(file='images/clear.png', height=50, width=50)
        self.fill_image = tk.PhotoImage(file='images/fill.png', height=50, width=50)
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
        
        # create frame widgets
        self.create_widgets()

    def create_widgets(self):
        # main canvas
        self.canvas = tk.Canvas(self, background='white')
        self.canvas.pack(expand=True, fill='both')

class SliderFrame(tk.Frame):
    def __init__(self, window):
        super().__init__(window, bg='white')