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
        self.frame_left.grid_rowconfigure(10, weight=1)

        #Example queries
        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Example query #1",
                                                command=self.example_query_1,
                                                hover="bla")
        self.button_1.grid(pady=(10, 0), padx=(50, 50), row=0, column=0)
        self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Example query #2",
                                                command=self.example_query_2)
        self.button_2.grid(pady=(10, 0), padx=(50, 50), row=1, column=0)
        self.button_3 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Example query #3",
                                                command=self.example_query_3)
        self.button_3.grid(pady=(10, 0), padx=(50, 50), row=2, column=0)


        self.button_4 = customtkinter.CTkOptionMenu(self.frame_left, values=["None","Europe", "Africa","Asia"],
                                                                       command=self.change_map)
        self.button_4.grid(row=3, column=0, padx=(20, 20), pady=(10, 0))
        self.button_4.set("Continents")

        self.button_5 = customtkinter.CTkOptionMenu(self.frame_left, values=["None", "GDP", "Obesity"],
                                                                       command=self.change_map)
        self.button_5.grid(row=4, column=0, padx=(20, 20), pady=(10, 0))
        self.button_5.set("Type")

        self.button_6 = customtkinter.CTkOptionMenu(self.frame_left, values=["5", "10", "15", "20"],
                                                                       command=self.change_map)
        self.button_6.grid(row=5, column=0, padx=(20, 20), pady=(10, 0))
        self.button_6.set("Top #n")

        self.button_7 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Apply query")
        self.button_7.grid(pady=(10, 0), padx=(50, 50), row=6, column=0)
        

        ## right grid

        self.frame_right.grid_rowconfigure(1, weight=1)
        self.frame_right.grid_rowconfigure(0, weight=0)
        self.frame_right.grid_columnconfigure(0, weight=1)
        self.frame_right.grid_columnconfigure(1, weight=0)
        self.frame_right.grid_columnconfigure(2, weight=1)

        self.map_widget = TkinterMapView(self.frame_right, corner_radius=0)
        self.map_widget.grid(row=1, rowspan=1, column=0, columnspan=3, sticky="nswe", padx=(0, 0), pady=(0, 0))

        self.entry = customtkinter.CTkEntry(master=self.frame_right,
                                            placeholder_text="type address")
        self.entry.grid(row=0, column=0, sticky="we", padx=(12, 0), pady=12)
        self.entry.bind("<Return>", self.search_event)

        self.button_10 = customtkinter.CTkButton(master=self.frame_right,
                                                text="Search",
                                                width=90,
                                                command=self.search_event)
        self.button_10.grid(row=0, column=1, sticky="w", padx=(12, 0), pady=12)

        self.map_widget.set_address("Bergen")

    def start(self):
        self.mainloop()

    def on_closing(self, event=0):
        self.destroy()
    
    def new(self):

        new_window = customtkinter.CTkToplevel(fg_color="white")
        new_window.title("This is a new window!")
        new_window.geometry("600x400")
        new_window.resizable(False, True) # Width, Height

        def close():
            new_window.destroy()
            new_window.update()

	    # Close the window
        new_button = customtkinter.CTkButton(new_window, text="Close Window", command=close)
        new_button.pack(pady=40)

    def search_event(self, event=None):
        self.map_widget.set_address(self.entry.get())
    
    def change_map(self):
        return None
    
    def example_query_1(self):
        self.new()
    
    def example_query_2(self):
        return None
    
    def example_query_3(self):
        return None


if __name__ == "__main__":
    app = App()
    app.start()