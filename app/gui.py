import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
from PIL import Image, ImageTk
from app.model import text_model, image_model

class AppGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("HIT137 GUI")
        self.image_path = None
        self._build()

    def _build(self):
        top = tk.Frame(self.root); top.pack(fill="x")
        self.task = ttk.Combobox(top, values=["Text Generation","Image Classification"], state="readonly")
        self.task.current(0); self.task.pack(side="left", padx=5, pady=5)
        tk.Button(top, text="Run", command=self.run).pack(side="right", padx=5)
        tk.Button(top, text="Browse", command=self.browse).pack(side="right", padx=5)

        self.text_in = ScrolledText(self.root, height=5); self.text_in.pack(fill="x", padx=5, pady=5)
        self.out = ScrolledText(self.root, height=12); self.out.pack(fill="both", expand=True, padx=5, pady=5)
        self.preview = tk.Label(self.root, text="Image preview"); self.preview.pack(fill="both", expand=True)

    def browse(self):
        path = filedialog.askopenfilename(filetypes=[("Images","*.jpg *.png *.jpeg")])
        if path: 
            self.image_path = path
            img = Image.open(path).convert("RGB")
            img.thumbnail((200,200))
            self.photo = ImageTk.PhotoImage(img)
            self.preview.config(image=self.photo)

    def run(self):
        self.out.delete("1.0","end")
        if self.task.get() == "Text Generation":
            prompt = self.text_in.get("1.0","end").strip()
            if not prompt: 
                messagebox.showwarning("No input","Enter a prompt"); return
            res = text_model.run(prompt, max_new_tokens=30)
            self.out.insert("end", str(res))
        else:
            if not self.image_path:
                messagebox.showwarning("No image","Browse an image first"); return
            img = Image.open(self.image_path).convert("RGB")
            res = image_model.run(img)
            self.out.insert("end", str(res))

    def run_app(self):
        self.root.mainloop()
