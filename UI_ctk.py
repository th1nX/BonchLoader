import customtkinter
from customtkinter import filedialog

customtkinter.set_appearance_mode("dark")
mod_path = None
download_path = None


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("BONCH - Minecraft mod updater")
        self.geometry("350x190")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1), weight=1)

        self.button_frame = customtkinter.CTkFrame(self)
        self.button_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsw")
        self.title = customtkinter.CTkLabel(self.button_frame, text="Folders", fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")
        self.button_1 = customtkinter.CTkButton(self.button_frame, text="Mods", command=self.select_mod_folder)
        self.button_1.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")
        self.button_2 = customtkinter.CTkButton(self.button_frame, text="Download", command=self.select_download_folder)
        self.button_2.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="w")

        self.button_frame2 = customtkinter.CTkFrame(self)
        self.button_frame2.grid(row=0, column=1, padx=(0, 10), pady=(10, 0), sticky="nsw")
        self.title = customtkinter.CTkLabel(self.button_frame2, text="Version", fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        self.entry = customtkinter.CTkEntry(self.button_frame2, placeholder_text="Minecraft version")
        self.entry.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")
        self.combobox = customtkinter.CTkComboBox(self.button_frame2, values=["fabric", "forge"])
        self.combobox.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="w")

        self.button = customtkinter.CTkButton(self, text="Start update", command=self.start_update)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

    def start_update(self):
        version = self.entry.get()
        loader = self.combobox.get()
        print("START UPDATE", version, loader, download_path, mod_path)

    def select_mod_folder(self):
        global mod_path
        mod_path = filedialog.askdirectory()
        print(mod_path)

    def select_download_folder(self):
        global download_path
        download_path = filedialog.askdirectory()
        print(download_path)


app = App()
app.resizable(False, False)
app.mainloop()
