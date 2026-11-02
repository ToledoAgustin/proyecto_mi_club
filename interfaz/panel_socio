import tkinter as tk
from tkinter import ttk

class PanelSocio(tk.Toplevel):
    def __init__(self, master, socio):
        super().__init__(master)
        self.title("Panel del Socio")
        self.geometry("400x300")
        self.socio = socio
        
        lbl_bienvenida = ttk.Label(self, text=f"Bienvenido/a: {socio.nombre_completo}")
        lbl_usuario = ttk.Label(self, text=f"Usuario: {socio.get_usuario()}")
        lbl_estado = ttk.Label(self, text=f"Estado: {socio.estado}")
        lbl_rol = ttk.Label(self, text=f"Rol: {socio.rol}")
        btn_cerrar = ttk.Button(self, text="Cerrar", command=self.destroy)

        lbl_bienvenida.pack(pady=20)
        lbl_usuario.pack()
        lbl_estado.pack()
        lbl_rol.pack(pady=10)
        btn_cerrar.pack(pady=20)