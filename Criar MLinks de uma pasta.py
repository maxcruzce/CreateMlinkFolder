import os
import tkinter as tk
from tkinter import filedialog, font, ttk

def criar_link_simbolico(origem, destino):
    exit_code = os.system(f'mklink /D "{destino}" "{origem}"')
    if exit_code == 0:
        print(f"Link simbólico criado: {destino}")
    else:
        print(f"Falha ao criar link simbólico: {destino}. Código de saída: {exit_code}")

class LinkFrame(tk.Frame):
    def __init__(self, master=None, link_count=1, font=None):
        super().__init__(master)
        self.pack(pady=10)
        self.configure(bg='light grey')

        self.orig_label = tk.Label(self, text=f"Pasta original {link_count}:", font=font, bg='light grey')
        self.orig_label.pack(side=tk.LEFT)
        self.orig_entry = tk.Entry(self, font=font)
        self.orig_entry.pack(side=tk.LEFT)
        self.orig_button = tk.Button(self, text="Procurar", command=self.load_orig, font=font)
        self.orig_button.pack(side=tk.LEFT)

        self.dest_label = tk.Label(self, text=f"Destino do link {link_count}:", font=font, bg='light grey')
        self.dest_label.pack(side=tk.LEFT)
        self.dest_entry = tk.Entry(self, font=font)
        self.dest_entry.pack(side=tk.LEFT)
        self.dest_button = tk.Button(self, text="Procurar", command=self.load_dest, font=font)
        self.dest_button.pack(side=tk.LEFT)

        self.create_button = tk.Button(self, text="Criar Link", command=self.create_link, font=font)  # Alterado para "Criar Link"
        self.create_button.pack(side=tk.LEFT)

    def load_orig(self):
        diretorio = filedialog.askdirectory(title="Selecione a pasta original")
        self.orig_entry.delete(0, tk.END)
        self.orig_entry.insert(0, diretorio)

    def load_dest(self):
        diretorio = filedialog.askdirectory(title="Selecione o local do link")
        self.dest_entry.delete(0, tk.END)
        self.dest_entry.insert(0, diretorio)

    def create_link(self):
        origem = self.orig_entry.get()
        destino = os.path.join(self.dest_entry.get(), os.path.basename(origem))
        criar_link_simbolico(origem, destino)

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(padx=20, pady=20)  # Adiciona preenchimento ao redor da janela
        self.link_count = 0  # Inicializa link_count aqui
        self.fontStyle = font.Font(family="Lucida Grande", size=12)
        self.create_widgets()

    def create_widgets(self):
        self.add_link()  # Cria o primeiro conjunto de widgets ao iniciar o programa

        self.add_button = tk.Button(self, text="Adicionar Link Simbólico", command=self.add_link, font=self.fontStyle)
        self.add_button.pack(side=tk.BOTTOM, pady=10)  # O botão é posicionado na parte inferior

    def add_link(self):
        if self.link_count < 5:  # Limita o número de conjuntos de widgets a 5
            self.link_count += 1
            LinkFrame(self, link_count=self.link_count, font=self.fontStyle)
        else:
            print("Limite de links simbólicos alcançado.")

root = tk.Tk()
root.geometry("800x600")  # Define o tamanho da janela
root.configure(bg='light grey')
scrollbar = ttk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas = tk.Canvas(root, yscrollcommand=scrollbar.set, bg='light grey')
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=canvas.yview)

frame = tk.Frame(canvas, bg='light grey')
canvas.create_window((0,0), window=frame, anchor='nw')

app = Application(master=frame)
root.mainloop()
