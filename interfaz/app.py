import tkinter as tk
from tkinter import ttk

try:
    from PIL import Image, ImageTk
except ImportError:
    Image = None
    ImageTk = None

from interfaz.login import PantallaLogin
from interfaz.panel_admin import PanelAdmin
from interfaz.panel_socio import PanelSocio
from interfaz.tema import (
    BORDE,
    ENCABEZADO_TABLA,
    ESTADO_SUSPENDIDO,
    ETIQUETA,
    FILA_PAR,
    FONDO,
    FUENTE,
    FUENTE_GRANDE,
    FUENTE_MENU,
    FUENTE_NEGRITA,
    FUENTE_SUBTITULO,
    FUENTE_TABLA,
    LEMA_CLUB,
    NOMBRE_CLUB,
    PANEL,
    PRIMARIO,
    PRIMARIO_HOVER,
    RUTA_LOGO,
    SUBTITULO,
    TEXTO,
    TEXTO_CLARO,
    TEXTO_SUAVE,
)


class ClubApp(tk.Tk):
    """Ventana única que arma el encabezado, el menú y las pantallas."""

    def __init__(self):
        super().__init__()
        self.socio_actual = None
        self.panel = None
        self._botones_menu = []

        self.title(f"{NOMBRE_CLUB} | Sistema del club")
        self.geometry("950x650")
        self.minsize(850, 550)
        self.configure(bg=FONDO)

        self._estilizar_tablas()
        self._crear_encabezado()
        self._crear_cuerpo()
        self.mostrar_bienvenida()

        self.protocol("WM_DELETE_WINDOW", self.salir)

    # ── Armado general ─────────────────────────────────────────

    def _estilizar_tablas(self):
        """Aplica el tema del club a las tablas (ttk.Treeview).
        Se usa el tema 'clam' para que Windows respete los colores
        del encabezado."""
        estilo = ttk.Style(self)
        estilo.theme_use("clam")
        estilo.configure(
            "Club.Treeview",
            background=PANEL,
            fieldbackground=PANEL,
            foreground=TEXTO,
            rowheight=34,
            borderwidth=0,
            font=FUENTE_TABLA,
        )
        estilo.configure(
            "Club.Treeview.Heading",
            background=ENCABEZADO_TABLA,
            foreground=TEXTO,
            font=FUENTE_NEGRITA,
            relief="flat",
            borderwidth=0,
            padding=(8, 9),
        )
        estilo.map(
            "Club.Treeview",
            background=[("selected", PRIMARIO)],
            foreground=[("selected", TEXTO_CLARO)],
        )
        estilo.map(
            "Club.Treeview.Heading",
            background=[("active", BORDE)],
        )

    def _crear_encabezado(self):
        """Barra superior con el logo (o el nombre) del club."""
        encabezado = tk.Frame(self, bg=PRIMARIO, height=85)
        encabezado.pack(fill="x")
        encabezado.pack_propagate(False)

        self._logo = None
        self._logo_grande = None
        if RUTA_LOGO.exists():
            if Image is not None:
                original = Image.open(str(RUTA_LOGO))
                ancho_chico = 60
                alto_chico = round(original.height * ancho_chico / original.width)
                ancho_grande = 150
                alto_grande = round(original.height * ancho_grande / original.width)
                self._logo = ImageTk.PhotoImage(
                    original.resize((ancho_chico, alto_chico), Image.LANCZOS)
                )
                self._logo_grande = ImageTk.PhotoImage(
                    original.resize((ancho_grande, alto_grande), Image.LANCZOS)
                )
            else:
                self._logo = tk.PhotoImage(file=str(RUTA_LOGO))
            tk.Label(
                encabezado,
                image=self._logo,
                bg=PRIMARIO,
            ).pack(side="left", padx=25, pady=10)
        else:
            tk.Label(
                encabezado,
                text=NOMBRE_CLUB,
                font=FUENTE_SUBTITULO,
                bg=PRIMARIO,
                fg=TEXTO_CLARO,
            ).pack(side="left", padx=25, pady=15)

        tk.Label(
            encabezado,
            text=LEMA_CLUB,
            font=FUENTE_NEGRITA,
            bg=PRIMARIO,
            fg=TEXTO_CLARO,
        ).pack(side="right", padx=25)

        # Línea de acento debajo del encabezado
        tk.Frame(self, bg=PRIMARIO_HOVER, height=3).pack(fill="x")

    def _crear_cuerpo(self):
        """Contenedor central: menú a la izquierda, contenido a la derecha."""
        principal = tk.Frame(self, bg=FONDO)
        principal.pack(fill="both", expand=True)

        self.menu = tk.Frame(principal, bg=PANEL, width=210)
        self.menu.pack_propagate(False)

        self.contenido = tk.Frame(principal, bg=PANEL)

    # ── Utilidades de pantalla ─────────────────────────────────

    def limpiar_contenido(self):
        for elemento in self.contenido.winfo_children():
            elemento.destroy()

    def ocultar_menu(self):
        self.menu.pack_forget()
        self.contenido.pack_forget()
        self.contenido.pack(fill="both", expand=True)

    def mostrar_menu(self, panel):
        """Arma el menú lateral con los botones del panel actual."""
        for elemento in self.menu.winfo_children():
            elemento.destroy()
        self._botones_menu = []

        # Línea fina que separa el menú del contenido
        tk.Frame(self.menu, bg=BORDE, width=1).pack(side="right", fill="y")

        tk.Label(
            self.menu,
            text="MENÚ PRINCIPAL",
            font=("Arial", 9, "bold"),
            bg=PANEL,
            fg=TEXTO_SUAVE,
        ).pack(pady=(28, 14), padx=20, anchor="w")

        for texto, comando in panel.botones_menu():
            self.crear_boton_menu(texto, comando)

        # La primera opción (Inicio) arranca marcada
        if self._botones_menu:
            self._marcar_activo(self._botones_menu[0])

        self.contenido.pack_forget()
        self.menu.pack(side="left", fill="y")
        self.contenido.pack(
            side="right",
            fill="both",
            expand=True,
            padx=12,
            pady=12,
        )

    def _marcar_activo(self, activo):
        """Resalta en azul el botón de la sección actual."""
        for boton in self._botones_menu:
            if boton is activo:
                boton.config(bg=PRIMARIO, fg=TEXTO_CLARO)
            else:
                color = ESTADO_SUSPENDIDO if boton.cget("text") == "Cerrar sesión" else TEXTO
                boton.config(bg=PANEL, fg=color)

    def crear_boton_menu(self, texto, comando):
        es_salida = texto == "Cerrar sesión"
        color_texto = ESTADO_SUSPENDIDO if es_salida else TEXTO

        boton = tk.Button(
            self.menu,
            text=texto,
            font=FUENTE_MENU,
            bg=PANEL,
            fg=color_texto,
            activebackground=PRIMARIO,
            activeforeground=TEXTO_CLARO,
            relief="flat",
            bd=0,
            anchor="w",
            padx=20,
            pady=12,
            cursor="hand2",
        )

        def al_hacer_clic():
            if not es_salida:
                self._marcar_activo(boton)
            comando()

        boton.config(command=al_hacer_clic)

        def entrar(_e):
            if boton.cget("bg") != PRIMARIO:
                boton.config(bg=FILA_PAR)

        def salir(_e):
            if boton.cget("bg") != PRIMARIO:
                boton.config(bg=PANEL)

        boton.bind("<Enter>", entrar)
        boton.bind("<Leave>", salir)

        # Separación extra antes de "Cerrar sesión"
        boton.pack(fill="x", padx=10, pady=(22, 3) if es_salida else 3)
        self._botones_menu.append(boton)
        return boton

    def crear_boton(self, padre, texto, comando, ancho=25, borde=False):
        """Botón principal del club (color primario, sin relieve)."""
        boton = tk.Button(
            padre,
            text=texto,
            command=comando,
            bg=PRIMARIO,
            fg=TEXTO_CLARO,
            activebackground=PRIMARIO_HOVER,
            activeforeground=TEXTO_CLARO,
            font=FUENTE_NEGRITA,
            width=ancho,
            pady=8,
            relief="solid" if borde else "flat",
            bd=1 if borde else 0,
            cursor="hand2",
        )

        # Hover: se guardan los colores actuales para restaurarlos
        # (así funciona también si después se cambian bg/fg).
        colores = {}

        def entrar(_e):
            colores["bg"], colores["fg"] = boton.cget("bg"), boton.cget("fg")
            if str(boton["state"]) == "disabled":
                return
            boton.config(bg=FILA_PAR if borde else PRIMARIO_HOVER)

        def salir(_e):
            if colores:
                boton.config(bg=colores["bg"], fg=colores["fg"])

        boton.bind("<Enter>", entrar)
        boton.bind("<Leave>", salir)
        return boton

    # ── Pantallas de entrada ───────────────────────────────────

    def mostrar_bienvenida(self):
        self.limpiar_contenido()
        self.ocultar_menu()

        # Tarjeta centrada con borde fino
        tarjeta = tk.Frame(
            self.contenido,
            bg=PANEL,
            highlightbackground=BORDE,
            highlightthickness=1,
        )
        tarjeta.place(relx=0.5, rely=0.5, anchor="center")

        if self._logo is not None:
            tk.Label(tarjeta, image=self._logo_grande, bg=PANEL).pack(
                padx=70, pady=(35, 10)
            )

        tk.Label(
            tarjeta,
            text=NOMBRE_CLUB,
            font=FUENTE_GRANDE,
            bg=PANEL,
            fg=PRIMARIO,
        ).pack(padx=70, pady=(35 if self._logo is None else 10, 8))

        tk.Label(
            tarjeta,
            text=f"CLUB {NOMBRE_CLUB}",
            font=FUENTE_SUBTITULO,
            bg=PANEL,
            fg=TEXTO,
        ).pack(pady=4)

        tk.Label(
            tarjeta,
            text=SUBTITULO,
            font=FUENTE,
            bg=PANEL,
            fg=TEXTO_SUAVE,
        ).pack(pady=4)

        tk.Label(
            tarjeta,
            text=ETIQUETA,
            font=("Arial", 10, "bold"),
            bg=PANEL,
            fg=PRIMARIO,
        ).pack(pady=(8, 10))

        self.crear_boton(
            tarjeta,
            "INICIAR SESIÓN",
            self.mostrar_login,
            ancho=25,
        ).pack(pady=(20, 10))

        boton_salir = self.crear_boton(
            tarjeta,
            "SALIR",
            self.salir,
            ancho=25,
            borde=True,
        )
        boton_salir.config(bg=PANEL, fg=PRIMARIO)
        boton_salir.pack(pady=(0, 35))

    def mostrar_login(self):
        self.limpiar_contenido()
        self.ocultar_menu()
        PantallaLogin(self.contenido, self)

    # ── Transiciones de sesión ─────────────────────────────────

    def iniciar_sesion(self, socio):
        """Guarda el socio autenticado y abre su panel según el rol."""
        self.limpiar_contenido()
        self.socio_actual = socio
        if socio.es_administrador():
            self.panel = PanelAdmin(self, socio)
        else:
            self.panel = PanelSocio(self, socio)
        self.mostrar_menu(self.panel)
        self.panel.mostrar_inicio()

    def cerrar_sesion(self):
        self.socio_actual = None
        self.panel = None
        self.mostrar_bienvenida()

    def salir(self):
        self.destroy()