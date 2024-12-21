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
        self.window.bind('<ButtonRelease-1>', self.save)
        self.window.bind('<KeyPress-r>', self.restore_state_undo)

    def save(self, event):
        saved_canvas = tk.Canvas(self, background='white')
        saved_canvas.bind()
        saved_canvas.bind('<B1-Motion>', self.draw)
        saved_canvas.bind('<Button-1>', self.draw)
        saved_canvas.bind('<ButtonRelease-1>', self.save)
        saved_canvas.bind('<KeyPress-r>', self.restore_state_undo)

        canvas_state = self.canvas.find_all()
        for obj in canvas_state:
            # Get object type (e.g., line, rectangle, oval, etc.)
            obj_type = self.canvas.type(obj)
            
            # Get object coordinates
            coords = self.canvas.coords(obj)
            
            # Get all configurable attributes
            attributes = self.canvas.itemconfig(obj)
            
            # Prepare attributes dictionary for new object
            new_attributes = {attr: details[-1] for attr, details in attributes.items()}
            
            # Create the same object on the new canvas
            if obj_type == "line":
                saved_canvas.create_line(*coords, **new_attributes)
            elif obj_type == "rectangle":
                saved_canvas.create_rectangle(*coords, **new_attributes)
            elif obj_type == "oval":
                saved_canvas.create_oval(*coords, **new_attributes)
            elif obj_type == "text":
                saved_canvas.create_text(*coords, **new_attributes)
            elif obj_type == "polygon":
                saved_canvas.create_polygon(*coords, **new_attributes)

        self.window.undo_list.append(saved_canvas)
        print("saved")

    def restore_state_undo(self, event):
        canvas_to_restore = self.window.undo_list[len(self.window.undo_list) - 1]
        self.window.undo_list.remove(canvas_to_restore)
        self.canvas.pack_forget()
        self.create_widgets()

        # Get all objects from the saved canvas
        saved_state = canvas_to_restore.find_all()

        for obj in saved_state:
            # Get object type (e.g., line, rectangle, oval, etc.)
            obj_type = canvas_to_restore.type(obj)
            
            # Get object coordinates
            coords = canvas_to_restore.coords(obj)
            
            # Get all configurable attributes
            attributes = canvas_to_restore.itemconfig(obj)
            
            # Prepare attributes dictionary for the new object
            new_attributes = {attr: details[-1] for attr, details in attributes.items()}
            
            # Recreate the object on the target canvas
            if obj_type == "line":
                self.canvas.create_line(*coords, **new_attributes)
            elif obj_type == "rectangle":
                self.canvas.create_rectangle(*coords, **new_attributes)
            elif obj_type == "oval":
                self.canvas.create_oval(*coords, **new_attributes)
            elif obj_type == "text":
                self.canvas.create_text(*coords, **new_attributes)
            elif obj_type == "polygon":
                self.canvas.create_polygon(*coords, **new_attributes)
        print("restored")

    def restore_state_redo(self, event):
        print("restored")
        ind = len(self.window.undo_list) - 1
        canvas_to_restore = self.window.undo_list[ind]
        self.canvas.pack_forget()
        self.canvas = canvas_to_restore
    
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
