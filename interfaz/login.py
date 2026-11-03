import tkinter as tk
from servicios.servicio_autenticacion import autenticar
from .panel_admin import PanelAdmin
from .panel_socio import PanelSocio

class VentanaLogin(tk.Tk):
    def __init__(self):
        super().__init__()

        # --- Configuración de la Ventana ---
        self.title('App Mi Club - Nova Esports')
        self.geometry("394x600")
        self.resizable(False, False) # Opcional: evita que cambien el tamaño para mantener el diseño

        # Paleta de colores en tonos azules modernos
        self.fondo_principal = "#F0F4F8"   # Gris azulado muy suave de fondo
        self.blanco_puro = "#FFFFFF"
        self.texto_oscuro = "#1E293B"      # Azul pizarra muy oscuro para textos principales
        self.texto_secundario = "#64748B"  # Gris pizarra para subtítulos y etiquetas
        self.azul_primario = "#2563EB"     # Azul vibrante profesional para botones y acentos
        self.azul_hover = "#1D4ED8"        # Azul más oscuro para el hover del botón
        self.azul_claro = "#3B82F6"        # Azul brillante para destacar títulos

        self.configure(bg=self.fondo_principal)

        # --- Crear Interfaz ---
        self._crear_widgets()

        # Permite dar Enter para ingresar
        self.bind('<Return>', self.iniciar_sesion)

    def _crear_widgets(self):
        # --- Encabezado ---
        tk.Label(
            self, 
            text="Nova Esports", 
            bg=self.fondo_principal, 
            fg=self.azul_primario, 
            font=("Arial", 11, "bold")
        ).pack(pady=(45, 5))
        
        tk.Label(
            self, 
            text="Iniciar Sesión", 
            bg=self.fondo_principal, 
            fg=self.texto_oscuro, 
            font=("Arial", 22, "bold")
        ).pack(pady=(0, 30))

        # --- Campos ---
        tk.Label(
            self, 
            text="Usuario / Email", 
            bg=self.fondo_principal, 
            fg=self.texto_secundario, 
            font=("Arial", 10, "bold")
        ).pack(anchor="w", padx=45, pady=(5, 5))
        
        self.entrada_usuario = tk.Entry(
            self, 
            bg=self.blanco_puro, 
            fg=self.texto_oscuro, 
            bd=1, 
            relief="solid", 
            font=("Arial", 11),
            highlightthickness=1,
            highlightcolor=self.azul_primario
        )
        self.entrada_usuario.pack(fill="x", padx=45, ipady=6, pady=(0, 15))

        tk.Label(
            self, 
            text="Contraseña", 
            bg=self.fondo_principal, 
            fg=self.texto_secundario, 
            font=("Arial", 10, "bold")
        ).pack(anchor="w", padx=45, pady=(5, 5))
        
        self.entrada_contrasenia = tk.Entry(
            self, 
            bg=self.blanco_puro, 
            fg=self.texto_oscuro, 
            show="*", 
            bd=1, 
            relief="solid", 
            font=("Arial", 11),
            highlightthickness=1,
            highlightcolor=self.azul_primario
        )
        self.entrada_contrasenia.pack(fill="x", padx=45, ipady=6, pady=(0, 15))

        # Etiqueta para errores
        self.etiqueta_mensaje = tk.Label(
            self, 
            text="", 
            bg=self.fondo_principal, 
            font=("Arial", 9, "bold")
        )
        self.etiqueta_mensaje.pack(pady=(0, 15))

        # --- Botón ---
        self.boton_ingresar = tk.Button(
            self, 
            text="Ingresar", 
            bg=self.azul_primario, 
            fg=self.blanco_puro, 
            activebackground=self.azul_hover, 
            activeforeground=self.blanco_puro, 
            font=("Arial", 11, "bold"), 
            bd=0, 
            cursor="hand2", 
            command=self.iniciar_sesion
        )
        self.boton_ingresar.pack(fill="x", padx=45, ipady=10, pady=(0, 10))

    def iniciar_sesion(self, event=None):
        usuario = self.entrada_usuario.get().strip()
        contrasenia = self.entrada_contrasenia.get().strip()
        
        # 1. Validar que los campos no estén vacíos
        if not usuario or not contrasenia:
            self.etiqueta_mensaje.config(text="Por favor, completa todos los campos", fg="#EF4444")
            return

        # 2. Llamar al servicio autenticar()
        socio = autenticar(usuario, contrasenia)

        if socio:
            self.etiqueta_mensaje.config(text="Iniciaste sesion correctamente", fg="#10B981")
            self.withdraw() # Ocultamos la ventana Login
        
        if socio:
            self.etiqueta_mensaje.config(text="")
            if socio.rol == "admin":
                PanelAdmin(self,socio)
            elif socio.rol == "socio":
                PanelSocio(self,socio)
        else:
            self.etiqueta_mensaje.config(text="Usuario o contraseña incorrectos", fg="#EF4444")