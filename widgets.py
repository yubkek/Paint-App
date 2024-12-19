from tkinter import ttk
import tkinter as tk

class Canvas:
    def __init__(self, window):
        self.canvas = tk.Canvas(window, bg='white')

class Button:
    def __init__(self, window):
        self.button = ttk.Button(window)

class Slider:
    def __init__(self, window):
        self.slider = ttk.Scale(window)

class Frame:
    def __init__(self, window):
        self.frame = tk.Frame(window, bg="red")