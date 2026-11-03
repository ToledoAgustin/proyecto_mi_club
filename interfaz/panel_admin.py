import tkinter as tk
from tkinter import ttk

class PanelAdmin(tk.Toplevel):
    def __init__(self, master, socio):
        super().__init__(master)
        self.title("Panel del Administrador")
        self.geometry("400x300")
        self.socio = socio
        
        lbl_admin = ttk.Label(self, text=f"Administrador: {socio.nombre_completo}")
        lbl_subtitulo = ttk.Label(self, text="Panel de gestión de socios")
        btn_cerrar = ttk.Button(self, text="Cerrar", command=self.destroy)

        lbl_admin.pack(pady=20)
        lbl_subtitulo.pack()
        btn_cerrar.pack(pady=20)