from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
import pickle

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
        self.eraser_button = tk.Button(self, image=self.eraser_image, command=lambda: self.window.set_color('white'))
        self.clear_button = tk.Button(self, image=self.clear_image, command=lambda: self.window.set_clear())
        self.fill_button = tk.Button(self, image=self.fill_image, command=lambda: self.window.set_fill())

        # undo and redo buttons
        self.undo_image = ImageTk.PhotoImage((Image.open('images/undo.png')).resize((120,120)))
        self.redo_image = ImageTk.PhotoImage((Image.open('images/redo.png')).resize((120,120)))
        self.undo_button = tk.Button(self, image=self.undo_image, command=lambda: self.window.event_generate("<KeyPress-r>"))
        self.redo_button = tk.Button(self, image=self.redo_image, command=lambda : self.window.event_generate("<KeyPress-s>"))

        # place
        self.black_button.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
        self.red_button.grid(row=4, column=0, sticky='nsew', padx=10, pady=10)
        self.blue_button.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)
        self.green_button.grid(row=3, column=0, sticky='nsew', padx=10, pady=10)
        self.yellow_button.grid(row=2, column=0, sticky='nsew', padx=10, pady=10)
        self.eraser_button.grid(row=0, column=1, sticky='nsew', padx=10, pady=10)
        self.clear_button.grid(row=2, column=1, sticky='nsew', padx=10, pady=10)
        self.fill_button.grid(row=1, column=1, sticky='nsew', padx=10, pady=10)

        self.undo_button.grid(row=3, column=1, sticky='nsew', padx=10, pady=10)
        self.redo_button.grid(row=4, column=1, sticky='nsew', padx=10, pady=10)


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
        self.canvas.bind('<B1-Motion>', self.draw)
        self.canvas.bind('<Button-1>', self.draw)
        self.window.bind('<ButtonRelease-1>', self.save)
        self.window.bind('<KeyPress-r>', self.restore_state_undo)
        self.window.bind('<KeyPress-s>', self.restore_state_redo)

    def get_options(self, options):
        return {
            key: value[-1]
            for key, value in options.items()
        }

    def save(self, event):
        if event.widget != self.canvas:
            return
        save_canvas = tk.Canvas(self, background='white')
        save_canvas.bind('<B1-Motion>', self.draw)
        save_canvas.bind('<Button-1>', self.draw)
        save_canvas.bind('<ButtonRelease-1>', self.save)
        save_canvas.bind('<KeyPress-r>', self.restore_state_undo)
        save_canvas.bind('<KeyPress-s>', self.restore_state_redo)

        for item_id in self.canvas.find_all():
                # Get item properties
                item_type = self.canvas.type(item_id)
                coords = self.canvas.coords(item_id)
                options = self.canvas.itemconfig(item_id)
                
                # Recreate the object in the target canvas
                if item_type == "rectangle":
                    save_canvas.create_rectangle(*coords, **self.get_options(options))
                elif item_type == "oval":
                    save_canvas.create_oval(*coords, **self.get_options(options))
                elif item_type == "line":
                    save_canvas.create_line(*coords, **self.get_options(options))
                elif item_type == "text":
                    save_canvas.create_text(*coords, **self.get_options(options))
                elif item_type == "polygon":
                    save_canvas.create_polygon(*coords, **self.get_options(options))
        self.window.undo_list.append(save_canvas)

    def restore_state_undo(self, event):
        if len(self.window.undo_list) > 0:
            self.canvas.pack_forget()
            self.window.redo_list.append(self.window.undo_list[-1])
            self.canvas = self.window.undo_list[-1]
            self.canvas.pack(expand=True, fill='both')
            self.window.undo_list = self.window.undo_list[:-1]

    def restore_state_redo(self, event):
        if len(self.window.redo_list) > 0:
            self.canvas.pack_forget()
            self.canvas = self.window.redo_list[-1]
            self.canvas.pack(expand=True, fill='both')
            self.window.redo_list = self.window.redo_list[:-1]
    
    def draw(self, event):
        if self.window.get_clear() == True:
            self.canvas.delete('all')
            self.window.set_clear()
        elif self.window.get_fill() == True:
            self.canvas.delete('all')
            self.canvas.create_rectangle((0,0,900,800), fill=self.window.get_color())
            self.window.set_fill()
        else:
            self.canvas.create_oval((event.x, 
                                    event.y, 
                                    event.x, 
                                    event.y), 
                                    fill=self.window.get_color(), 
                                    outline=self.window.get_color(),
                                    width=self.window.get_brush()
                                    )
        

class SliderFrame(tk.Frame):
    def __init__(self, window):
        super().__init__(window)
        self.window = window

        self.create_widgets()
    
    def create_widgets(self):
        self.scale = ttk.Scale(self, orient='horizontal', from_=1, to=50, length=600, variable=self.window.current_brush_size, command=self.update_circle)
        self.scale.place(relx=0.6, rely=0.5, anchor='center')

        self.create_circle()
    
    def create_circle(self):
        self.circle_canvas = tk.Canvas(self, background='white', width=150, height=150)
        self.circle_canvas.place(relx=0.02, rely=0.5, anchor='w')
        self.circle_canvas.create_oval((75,75,75,75), 
                                fill=self.window.get_color(), 
                                outline=self.window.get_color(),
                                width=self.window.get_brush()
                                )
        
    def update_circle(self, event):
        self.circle_canvas.pack_forget()
        self.create_circle()
