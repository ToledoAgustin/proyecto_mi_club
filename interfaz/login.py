import tkinter as tk
from servicios.servicio_autenticacion import autenticar

class VentanaLogin(tk.Tk):
    def __init__(self):
        super().__init__()

        # --- Configuración de la Ventana ---
        self.title('App Mi Club - Nova Esports')
        self.geometry("394x600")

        # Paleta de colores
        self.blanco_cremita = "#FAF7F2"
        self.blanco_puro = "#FFFFFF"
        self.marron_oscuro = "#3A332C"
        self.gris_calido = "#8C827A"
        self.beige = "#C49A6C"
        self.hover_oscuro = "#B3895B"

        self.configure(bg=self.blanco_cremita)

        # --- Crear Interfaz ---
        self._crear_widgets()

        # Permite dar Enter para ingresar
        self.bind('<Return>', self.iniciar_sesion)

    def _crear_widgets(self):
        # --- Encabezado ---
        tk.Label(self, text="Nova Esports", bg=self.blanco_cremita, fg=self.beige, font=("Arial", 11, "bold")).pack(pady=(40, 5))
        tk.Label(self, text="Iniciar Sesión", bg=self.blanco_cremita, fg=self.gris_calido, font=("Arial", 20, "bold")).pack(pady=(0, 25))

        # --- Campos ---
        tk.Label(self, text="Usuario / Email", bg=self.blanco_cremita, fg=self.gris_calido, font=("Arial", 10, "bold")).pack(anchor="w", padx=45, pady=(5, 5))
        self.entrada_usuario = tk.Entry(self, bg=self.blanco_puro, fg=self.marron_oscuro, bd=1, relief="solid", font=("Arial", 11))
        self.entrada_usuario.pack(fill="x", padx=45, ipady=6, pady=(0, 15))

        tk.Label(self, text="Contraseña", bg=self.blanco_cremita, fg=self.gris_calido, font=("Arial", 10, "bold")).pack(anchor="w", padx=45, pady=(5, 5))
        self.entrada_contrasenia = tk.Entry(self, bg=self.blanco_puro, fg=self.marron_oscuro, show="*", bd=1, relief="solid", font=("Arial", 11))
        self.entrada_contrasenia.pack(fill="x", padx=45, ipady=6, pady=(0, 15))

        # Etiqueta para errores
        self.etiqueta_mensaje = tk.Label(self, text="", bg=self.blanco_cremita, font=("Arial", 9, "bold"))
        self.etiqueta_mensaje.pack(pady=(0, 15))

        # --- Botón ---
        self.boton_ingresar = tk.Button(
            self, 
            text="Ingresar", 
            bg=self.beige, 
            fg=self.blanco_puro, 
            activebackground=self.hover_oscuro, 
            activeforeground=self.blanco_puro, 
            font=("Arial", 11, "bold"), 
            bd=0, 
            cursor="hand2", 
            command=self.iniciar_sesion
        )
        self.boton_ingresar.pack(fill="x", padx=45, ipady=8, pady=(0, 10))

    def iniciar_sesion(self, event=None):
        usuario = self.entrada_usuario.get().strip()
        contrasenia = self.entrada_contrasenia.get().strip()
        
        # 1. Validar que los campos no estén vacíos
        if not usuario or not contrasenia:
            self.etiqueta_mensaje.config(text="Por favor, completa todos los campos", fg="#C0392B")
            return

        # 2. Llamar al servicio autenticar()
        socio = autenticar(usuario, contrasenia)
        
        if socio:
            self.etiqueta_mensaje.config(text="")
            # 3. Mirar socio.rol para decidir qué panel abrir
            if socio.rol == "admin":
                self.abrir_panel_admin(socio)
            elif socio.rol == "socio":
                self.abrir_panel_socio(socio)
        else:
            # 4. Mismo mensaje genérico si falla
            self.etiqueta_mensaje.config(text="Usuario o contraseña incorrectos", fg="#C0392B")

    def abrir_panel_admin(self, socio):
        self.destroy()
        # Lanzar la ventana de admin aquí

    def abrir_panel_socio(self, socio):
        self.destroy()
        # Lanzar la ventana de socio aquí