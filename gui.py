import customtkinter
from tkintermapview import TkinterMapView
from tkinter import ttk
import tkinter as tk

customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):

    APP_NAME = "TkinterMapView with CustomTkinter"
    WIDTH = 800
    HEIGHT = 500

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title(App.APP_NAME)
        self.geometry(str(App.WIDTH) + "x" + str(App.HEIGHT))
        self.minsize(App.WIDTH, App.HEIGHT)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.bind("<Command-q>", self.on_closing)
        self.bind("<Command-w>", self.on_closing)
        self.createcommand('tk::mac::Quit', self.on_closing)

        self.marker_list = []

        # ============ create two CTkFrames ============

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self, width=350, corner_radius=0, fg_color=None)
        self.frame_left.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

        self.frame_right = customtkinter.CTkFrame(master=self, corner_radius=0)
        self.frame_right.grid(row=0, column=1, rowspan=1, pady=0, padx=0, sticky="nsew")

        ## Left grid
        self.frame_left.grid_rowconfigure(4, weight=1)

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Set Marker")
        self.button_1.grid(pady=(10, 0), padx=(50, 50), row=0, column=0)

        self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Clear Markers")
        self.button_2.grid(pady=(10, 0), padx=(50, 50), row=1, column=0)

        self.map_label = customtkinter.CTkLabel(self.frame_left, text="Countries:", anchor="w")
        self.map_label.grid(row=2, column=0, padx=(20, 20), pady=(10, 0))

        self.button_3 = customtkinter.CTkOptionMenu(self.frame_left, values=["Berlin", "Oslo","Paris"],
                                                                       command=self.change_map)
        self.button_3.grid(row=3, column=0, padx=(20, 20), pady=(10, 0))
        self.button_3.set("Insert")

        ## right grid

        self.frame_right.grid_rowconfigure(1, weight=1)
        self.frame_right.grid_rowconfigure(0, weight=0)
        self.frame_right.grid_columnconfigure(0, weight=1)
        self.frame_right.grid_columnconfigure(1, weight=0)
        self.frame_right.grid_columnconfigure(2, weight=1)

        self.map_widget = TkinterMapView(self.frame_right, corner_radius=0)
        self.map_widget.grid(row=1, rowspan=1, column=0, columnspan=3, sticky="nswe", padx=(0, 0), pady=(0, 0))
        self.map_widget.set_address("Berlin")

    def start(self):
        self.mainloop()

    def on_closing(self, event=0):
        self.destroy()
    
    def change_map():
        return None


if __name__ == "__main__":
    app = App()
    app.start()