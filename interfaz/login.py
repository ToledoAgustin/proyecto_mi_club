import tkinter as tk
from tkinter import messagebox

from interfaz.tema import (
    BORDE,
    CAMPO,
    FUENTE,
    FUENTE_CHICA,
    FUENTE_NEGRITA,
    FUENTE_TITULO,
    NOMBRE_CLUB,
    PANEL,
    PRIMARIO,
    PRIMARIO_HOVER,
    TEXTO,
    TEXTO_SUAVE,
)
from servicios.servicio_autenticacion import autenticar


class PantallaLogin(tk.Frame):
    """Formulario de ingreso. Al validar, avisa a la app principal."""

    def __init__(self, padre, app):
        super().__init__(padre, bg=PANEL)
        self.app = app
        self.pack(fill="both", expand=True)
        self._crear_widgets()

    def _crear_campo(self, padre, oculto=False):
        """Campo de texto con borde fino que se pinta de azul al
        hacer foco. Devuelve (marco, entrada)."""
        marco = tk.Frame(
            padre,
            bg=CAMPO,
            highlightbackground=BORDE,
            highlightthickness=1,
        )
        entrada = tk.Entry(
            marco,
            font=FUENTE,
            width=30,
            show="*" if oculto else "",
            bg=CAMPO,
            fg=TEXTO,
            relief="flat",
            bd=0,
            insertbackground=TEXTO,
        )
        entrada.pack(side="left", fill="x", expand=True,
                     padx=(10, 4), pady=8)

        entrada.bind(
            "<FocusIn>",
            lambda _e: marco.config(highlightbackground=PRIMARIO),
        )
        entrada.bind(
            "<FocusOut>",
            lambda _e: marco.config(highlightbackground=BORDE),
        )
        return marco, entrada

    def _crear_widgets(self):
        # Tarjeta centrada con borde fino
        tarjeta = tk.Frame(
            self,
            bg=PANEL,
            highlightbackground=BORDE,
            highlightthickness=1,
        )
        tarjeta.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(
            tarjeta,
            text="INICIAR SESIÓN",
            font=FUENTE_TITULO,
            bg=PANEL,
            fg=PRIMARIO,
        ).pack(padx=60, pady=(35, 6))

        tk.Label(
            tarjeta,
            text=f"Ingresá con tu cuenta de {NOMBRE_CLUB}.",
            font=FUENTE,
            bg=PANEL,
            fg=TEXTO_SUAVE,
        ).pack(pady=(0, 5))

        formulario = tk.Frame(tarjeta, bg=PANEL)
        formulario.pack(padx=60, pady=20)

        tk.Label(
            formulario,
            text="Usuario",
            font=FUENTE_NEGRITA,
            bg=PANEL,
            fg=TEXTO,
        ).pack(anchor="w")

        marco_usuario, self.entrada_usuario = self._crear_campo(formulario)
        marco_usuario.pack(fill="x", pady=(5, 16))

        tk.Label(
            formulario,
            text="Contraseña",
            font=FUENTE_NEGRITA,
            bg=PANEL,
            fg=TEXTO,
        ).pack(anchor="w")

        marco_contrasenia, self.entrada_contrasenia = self._crear_campo(
            formulario, oculto=True
        )
        marco_contrasenia.pack(fill="x", pady=(5, 0))

        # El botón Mostrar/Ocultar queda dentro del mismo campo
        self.boton_ver = tk.Button(
            marco_contrasenia,
            text="Mostrar",
            font=FUENTE_CHICA,
            bg=CAMPO,
            fg=PRIMARIO,
            activebackground=CAMPO,
            activeforeground=PRIMARIO_HOVER,
            relief="flat",
            bd=0,
            cursor="hand2",
            command=self._alternar_contrasenia,
        )
        self.boton_ver.pack(side="right", padx=(0, 8))

        self.app.crear_boton(
            tarjeta,
            "INGRESAR",
            self._ingresar,
            ancho=30,
        ).pack(padx=60, pady=(10, 8))

        volver = tk.Button(
            tarjeta,
            text="← Volver al inicio",
            font=FUENTE,
            bg=PANEL,
            fg=TEXTO_SUAVE,
            activebackground=PANEL,
            activeforeground=PRIMARIO,
            relief="flat",
            bd=0,
            cursor="hand2",
            command=self.app.mostrar_bienvenida,
        )
        volver.pack(pady=(0, 30))
        volver.bind("<Enter>", lambda _e: volver.config(fg=PRIMARIO))
        volver.bind("<Leave>", lambda _e: volver.config(fg=TEXTO_SUAVE))

        self.entrada_usuario.focus()
        self.bind("<Return>", lambda evento: self._ingresar())
        # Enter también desde los campos (el evento no llega al frame)
        self.entrada_usuario.bind("<Return>", lambda evento: self._ingresar())
        self.entrada_contrasenia.bind("<Return>", lambda evento: self._ingresar())

    def _alternar_contrasenia(self):
        if self.entrada_contrasenia.cget("show") == "*":
            self.entrada_contrasenia.configure(show="")
            self.boton_ver.configure(text="Ocultar")
        else:
            self.entrada_contrasenia.configure(show="*")
            self.boton_ver.configure(text="Mostrar")

    def _ingresar(self):
        usuario = self.entrada_usuario.get().strip()
        contrasenia = self.entrada_contrasenia.get()

        if not usuario or not contrasenia:
            messagebox.showwarning(
                "Campos incompletos",
                "Completá el usuario y la contraseña.",
            )
            return

        socio = autenticar(usuario, contrasenia)
        if socio is None:
            messagebox.showerror(
                "Error de acceso",
                "Usuario o contraseña incorrectos.",
            )
            self.entrada_contrasenia.delete(0, tk.END)
            self.entrada_contrasenia.focus()
            return

        self.app.iniciar_sesion(socio)