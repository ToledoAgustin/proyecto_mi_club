import re
import tkinter as tk
from tkinter import messagebox, ttk

from interfaz.tema import (
    BORDE,
    ENCABEZADO_TABLA,
    ESTADO_ACTIVO,
    ESTADO_ACTIVO_HOVER,
    ESTADO_PENDIENTE,
    ESTADO_SUSPENDIDO,
    ESTADO_VENCIDO,
    FILA_PAR,
    FILA_SUSPENDIDO,
    FILA_SUSPENDIDO_PAR,
    FUENTE,
    FUENTE_CHICA,
    FUENTE_NEGRITA,
    FUENTE_TITULO,
    PANEL,
    PRIMARIO,
    TEXTO,
    TEXTO_CLARO,
    TEXTO_SUAVE,
)
from servicios.servicios_cuota  import listar_cuotas, pagar_cuota
from servicios.servicios_socios import listar_clubes_de_socio, obtener_socio


class PanelSocio(tk.Frame):
    """Pantallas que ve el socio dentro de la ventana principal."""

    def __init__(self, app, socio):
        super().__init__(app.contenido, bg=PANEL)
        self.app = app
        self.usuario = socio.get_usuario()
        self._periodos = []
        self._configurar_estilos()
        self.pack(fill="both", expand=True)

    # ── Estilos ────────────────────────────────────────────────

    def _configurar_estilos(self):
        """Estilo de la tabla (tema 'clam' para que se vean los
        encabezados en Windows)."""
        estilo = ttk.Style()
        estilo.theme_use("clam")

        estilo.configure(
            "Club.Treeview",
            background=PANEL,
            fieldbackground=PANEL,
            foreground=TEXTO,
            rowheight=34,
            borderwidth=0,
            font=("Arial", 10),
        )
        estilo.configure(
            "Club.Treeview.Heading",
            background=ENCABEZADO_TABLA,
            foreground=TEXTO,
            font=("Arial", 10, "bold"),
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

    # ── Utilidades ─────────────────────────────────────────────

    def botones_menu(self):
        return [
            ("Inicio", self.mostrar_inicio),
            ("Mis datos", self.mostrar_datos),
            ("Mis clubes", self.mostrar_clubes),
            ("Mis cuotas", self.mostrar_cuotas),
            ("Cerrar sesión", self.app.cerrar_sesion),
        ]

    def _limpiar(self):
        for elemento in self.winfo_children():
            elemento.destroy()

    def _crear_titulo(self, texto, subtitulo=None):
        tk.Label(
            self,
            text=texto,
            font=FUENTE_TITULO,
            bg=PANEL,
            fg=PRIMARIO,
        ).pack(pady=(18, 2 if subtitulo else 12))

        if subtitulo:
            tk.Label(
                self,
                text=subtitulo,
                font=FUENTE_CHICA,
                bg=PANEL,
                fg=TEXTO_SUAVE,
            ).pack(pady=(0, 12))

    def _etiqueta_estado(self, estado):
        if estado == "Suspendido":
            return ESTADO_SUSPENDIDO
        return ESTADO_ACTIVO

    def _crear_boton_accion(self, padre, texto, comando, color, color_hover):
        boton = tk.Button(
            padre,
            text=texto,
            command=comando,
            font=FUENTE_NEGRITA,
            bg=color,
            fg=TEXTO_CLARO,
            activebackground=color_hover,
            activeforeground=TEXTO_CLARO,
            disabledforeground="#CBD5E1",
            relief="flat",
            bd=0,
            padx=26,
            pady=9,
            cursor="hand2",
        )

        def entrar(_e):
            if str(boton["state"]) != "disabled":
                boton.config(bg=color_hover)

        boton.bind("<Enter>", entrar)
        boton.bind("<Leave>", lambda _e: boton.config(bg=color))
        return boton

    # ── Pantallas ──────────────────────────────────────────────

    def mostrar_inicio(self):
        self._limpiar()
        socio = obtener_socio(self.usuario)

        if socio is None:
            messagebox.showerror("Error", "El socio ya no existe.")
            self.app.cerrar_sesion()
            return

        self._crear_titulo(
            f"¡Bienvenido/a, {socio.nombre_completo}!",
            "Este es el resumen de tu cuenta",
        )

        cuotas = listar_cuotas(self.usuario)
        pendientes = [
            cuota for cuota in cuotas if cuota.get_estado() in ("Pendiente", "Vencida")
        ]

        tarjeta = tk.Frame(self, bg=PANEL)
        tarjeta.pack(pady=20)

        self._crear_tarjeta(tarjeta, "Estado", socio.estado,
                            self._etiqueta_estado(socio.estado)).grid(
            row=0, column=0, padx=14)

        self._crear_tarjeta(tarjeta, "Cuotas pendientes", str(len(pendientes)),
                            ESTADO_PENDIENTE).grid(row=0, column=1, padx=14)

        tk.Label(
            self,
            text="Usá el menú para ver tus datos, tus clubes y tus cuotas.",
            font=FUENTE,
            bg=PANEL,
            fg=TEXTO_SUAVE,
        ).pack(pady=15)

    def _crear_tarjeta(self, padre, titulo, valor, color):
        tarjeta = tk.Frame(padre, bg=PANEL, highlightbackground=BORDE,
                           highlightthickness=1)
        # Franja de color arriba de la tarjeta
        tk.Frame(tarjeta, bg=color, height=5).pack(fill="x")
        tk.Label(
            tarjeta,
            text=str(valor),
            font=("Arial", 30, "bold"),
            bg=PANEL,
            fg=color,
            width=9,
        ).pack(padx=24, pady=(18, 2))
        tk.Label(
            tarjeta,
            text=titulo.upper(),
            font=("Arial", 9, "bold"),
            bg=PANEL,
            fg=TEXTO_SUAVE,
        ).pack(padx=24, pady=(0, 18))
        return tarjeta

    def mostrar_datos(self):
        self._limpiar()
        socio = obtener_socio(self.usuario)

        if socio is None:
            messagebox.showerror("Error", "El socio ya no existe.")
            self.app.cerrar_sesion()
            return

        self._crear_titulo("MIS DATOS", "Información de tu cuenta en el club")

        tabla = tk.Frame(self, bg=PANEL, highlightbackground=BORDE,
                         highlightthickness=1)
        tabla.pack(pady=10, ipadx=30, ipady=10)

        valores = [
            ("Nombre completo", socio.nombre_completo),
            ("Edad", socio.edad),
            ("Identificación",
             f"{socio.get_tipo_identificacion()} {socio.get_identificacion()}"),
            ("Nacionalidad", socio.get_nacionalidad()),
            ("Fecha de inscripción", socio.fecha_inscripcion),
        ]

        for fila, (etiqueta, valor) in enumerate(valores):
            tk.Label(
                tabla,
                text=f"{etiqueta}:",
                font=FUENTE_NEGRITA,
                bg=PANEL,
                fg=TEXTO_SUAVE,
            ).grid(row=fila, column=0, sticky="e", padx=(24, 14), pady=7)

            tk.Label(
                tabla,
                text=valor,
                font=FUENTE,
                bg=PANEL,
                fg=TEXTO,
            ).grid(row=fila, column=1, sticky="w", padx=(0, 24), pady=7)

        tk.Label(
            tabla,
            text="Estado:",
            font=FUENTE_NEGRITA,
            bg=PANEL,
            fg=TEXTO_SUAVE,
        ).grid(row=len(valores), column=0, sticky="e", padx=(24, 14), pady=7)

        tk.Label(
            tabla,
            text=f"● {socio.estado}",
            font=FUENTE_NEGRITA,
            bg=PANEL,
            fg=self._etiqueta_estado(socio.estado),
        ).grid(row=len(valores), column=1, sticky="w", padx=(0, 24), pady=7)

    def mostrar_clubes(self):
        self._limpiar()
        self._crear_titulo("MIS CLUBES", "Clubes a los que pertenecés")

        try:
            clubes = listar_clubes_de_socio(self.usuario)

            if not clubes:
                tk.Label(
                    self,
                    text="Sin clubes asociados",
                    font=FUENTE,
                    bg=PANEL,
                    fg=TEXTO_SUAVE,
                ).pack(pady=25)
                return

            for club in clubes:
                fila = tk.Frame(self, bg=PANEL, highlightbackground=BORDE,
                                highlightthickness=1)
                fila.pack(fill="x", padx=40, pady=5)

                # Franja azul a la izquierda de cada club
                tk.Frame(fila, bg=PRIMARIO, width=5).pack(side="left", fill="y")

                # Solo presentación: se parte el texto de mostrar_info()
                # en sus datos para mostrar cada uno en su línea.
                partes = re.split(
                    r", (?=[A-ZÁÉÍÓÚ][\wáéíóúñ ]*: |El club tiene)",
                    club.mostrar_info(),
                )

                cuerpo = tk.Frame(fila, bg=PANEL)
                cuerpo.pack(side="left", fill="x", expand=True, padx=16, pady=10)

                for numero, parte in enumerate(partes):
                    if numero == 0:
                        texto = parte.replace("Nombre: ", "", 1)
                        fuente, color = ("Arial", 12, "bold"), PRIMARIO
                    else:
                        texto = parte
                        fuente, color = FUENTE, TEXTO
                    tk.Label(
                        cuerpo,
                        text=texto,
                        font=fuente,
                        bg=PANEL,
                        fg=color,
                        anchor="w",
                        justify="left",
                        wraplength=450,
                    ).pack(fill="x", pady=1)

        except Exception as error:
            tk.Label(
                self,
                text=f"Error al mostrar los clubes:\n{error}",
                font=FUENTE,
                bg=PANEL,
                fg=ESTADO_SUSPENDIDO,
                justify="left",
                wraplength=600,
            ).pack(pady=20)

    def mostrar_cuotas(self):
        self._limpiar()
        self._crear_titulo(
            "MIS CUOTAS",
            "Seleccioná una cuota de la lista para pagarla",
        )

        contenedor = tk.Frame(self, bg=PANEL, highlightbackground=BORDE,
                              highlightthickness=1)
        contenedor.pack(fill="both", expand=True, padx=40, pady=(0, 12))

        columnas = ("periodo", "estado", "vencimiento")
        tabla = ttk.Treeview(
            contenedor,
            columns=columnas,
            show="headings",
            style="Club.Treeview",
            height=10,
            selectmode="browse",
        )
        tabla.heading("periodo", text="Período")
        tabla.heading("estado", text="Estado")
        tabla.heading("vencimiento", text="Fecha de vencimiento")
        tabla.column("periodo", width=170, anchor="center")
        tabla.column("estado", width=150, anchor="center")
        tabla.column("vencimiento", width=200, anchor="center")

        # Un solo tag por fila (estado + rayado) para que los colores
        # no se pisen entre sí.
        colores = {
            "Pagada": (ESTADO_ACTIVO, FILA_PAR, PANEL),
            "Pendiente": (ESTADO_PENDIENTE, FILA_PAR, PANEL),
            "Vencida": (ESTADO_VENCIDO, FILA_SUSPENDIDO_PAR, FILA_SUSPENDIDO),
        }
        for estado, (texto, fondo_par, fondo_impar) in colores.items():
            tabla.tag_configure(f"{estado}_par", background=fondo_par,
                                foreground=texto)
            tabla.tag_configure(f"{estado}_impar", background=fondo_impar,
                                foreground=texto)
        tabla.tag_configure("par", background=FILA_PAR, foreground=TEXTO)
        tabla.tag_configure("impar", background=PANEL, foreground=TEXTO)

        barra = ttk.Scrollbar(contenedor, orient="vertical",
                              command=tabla.yview)
        tabla.configure(yscrollcommand=barra.set)
        barra.pack(side="right", fill="y")
        tabla.pack(side="left", fill="both", expand=True)

        boton_pagar = self._crear_boton_accion(
            self,
            "PAGAR CUOTA SELECCIONADA",
            lambda: self._pagar(tabla),
            ESTADO_ACTIVO,
            ESTADO_ACTIVO_HOVER,
        )
        boton_pagar.pack(pady=(0, 16))

        self._cargar_cuotas(tabla, boton_pagar)

    def _cargar_cuotas(self, tabla, boton_pagar):
        for fila in tabla.get_children():
            tabla.delete(fila)
        self._periodos = []

        cuotas = listar_cuotas(self.usuario)

        if not cuotas:
            tk.Label(
                self,
                text="Sin cuotas cargadas",
                font=FUENTE,
                bg=PANEL,
                fg=TEXTO_SUAVE,
            ).pack(pady=10)
            boton_pagar.configure(state="disabled")
            return

        boton_pagar.configure(state="normal")
        for indice, cuota in enumerate(cuotas):
            rayado = "par" if indice % 2 == 0 else "impar"
            estado = cuota.get_estado()
            etiqueta = f"{estado}_{rayado}" if estado in ("Pagada", "Pendiente", "Vencida") else rayado
            tabla.insert(
                "",
                "end",
                values=(cuota.periodo, estado, cuota.fecha_de_vencimiento),
                tags=(etiqueta,),
            )
            self._periodos.append(cuota.periodo)

    def _pagar(self, tabla):
        seleccion = tabla.selection()
        if not seleccion or not self._periodos:
            messagebox.showwarning("Aviso", "Seleccioná una cuota primero.")
            return

        indice = tabla.index(seleccion[0])
        periodo = self._periodos[indice]

        mensaje = pagar_cuota(self.usuario, periodo)
        messagebox.showinfo("Pagar cuota", mensaje)

        self.mostrar_cuotas()