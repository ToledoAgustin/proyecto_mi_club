import tkinter as tk
from tkinter import messagebox, ttk
from datetime import date

from interfaz.tema import (
    BORDE,
    CAMPO,
    ENCABEZADO_TABLA,
    ESTADO_ACTIVO,
    ESTADO_ACTIVO_HOVER,
    ESTADO_SUSPENDIDO,
    ESTADO_SUSPENDIDO_HOVER,
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
from servicios.servicios_cuota import listar_cuotas
from servicios.servicios_socios import (
    listar_socios,
    obtener_socio,
    reactivar_socio,
    registrar_socio,
    suspender_socio,
)

CAMPOS_REGISTRO = [
    ("Nombre completo *", "nombre", ""),
    ("Edad", "edad", ""),
    ("Tipo de identificación", "tipo_identificacion", ""),
    ("Identificación *", "identificacion", ""),
    ("Nacionalidad", "nacionalidad", ""),
    ("Usuario único *", "usuario", ""),
    ("Contraseña *", "contrasenia", "*"),
]


class PanelAdmin(tk.Frame):
    """Pantallas que ve el administrador dentro de la ventana principal."""

    def __init__(self, app, socio):
        super().__init__(app.contenido, bg=PANEL)
        self.app = app
        self.usuario = socio.get_usuario()
        self._usuarios = []
        self._configurar_estilos()
        self.pack(fill="both", expand=True)

    # ── Estilos ────────────────────────────────────────────────

    def _configurar_estilos(self):
        """Estilo de la tabla. Se usa el tema 'clam' porque el tema por
        defecto de Windows ignora los colores del encabezado (por eso
        no se veían los títulos de las columnas)."""
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
        estilo.configure(
            "Club.Vertical.TScrollbar",
            background=BORDE,
            troughcolor=PANEL,
            borderwidth=0,
            arrowsize=14,
        )

    # ── Utilidades ─────────────────────────────────────────────

    def botones_menu(self):
        return [
            ("Inicio", self.mostrar_inicio),
            ("Socios", self.mostrar_socios),
            ("Registrar socio", self.mostrar_registro),
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
            relief="flat",
            bd=0,
            padx=26,
            pady=9,
            cursor="hand2",
        )
        boton.bind("<Enter>", lambda _e: boton.config(bg=color_hover))
        boton.bind("<Leave>", lambda _e: boton.config(bg=color))
        return boton

    # ── Pantallas ──────────────────────────────────────────────

    def mostrar_inicio(self):
        self._limpiar()
        self._crear_titulo(
            "PANEL DE ADMINISTRACIÓN",
            "Resumen general del club",
        )

        socios = listar_socios()
        activos = [s for s in socios if s.estado == "Activo"]
        suspendidos = [s for s in socios if s.estado == "Suspendido"]

        tarjeta = tk.Frame(self, bg=PANEL)
        tarjeta.pack(pady=20)

        self._crear_tarjeta(tarjeta, "Socios registrados", str(len(socios)),
                            PRIMARIO).grid(row=0, column=0, padx=14)

        self._crear_tarjeta(tarjeta, "Activos", str(len(activos)),
                            ESTADO_ACTIVO).grid(row=0, column=1, padx=14)

        self._crear_tarjeta(tarjeta, "Suspendidos", str(len(suspendidos)),
                            ESTADO_SUSPENDIDO).grid(row=0, column=2, padx=14)

        tk.Label(
            self,
            text=f"Sesión de {self.usuario}. "
                 "Desde el menú podés gestionar los socios.",
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
            width=7,
        ).pack(padx=24, pady=(18, 2))
        tk.Label(
            tarjeta,
            text=titulo.upper(),
            font=("Arial", 9, "bold"),
            bg=PANEL,
            fg=TEXTO_SUAVE,
        ).pack(padx=24, pady=(0, 18))
        return tarjeta

    def mostrar_socios(self):
        self._limpiar()
        self._crear_titulo(
            "SOCIOS DEL CLUB",
            "Seleccioná un socio de la lista para suspenderlo o reactivarlo",
        )

        contenedor = tk.Frame(self, bg=PANEL, highlightbackground=BORDE,
                              highlightthickness=1)
        contenedor.pack(fill="both", expand=True, padx=30, pady=(0, 12))

        columnas = ("usuario", "nombre", "estado", "inscripcion", "pendientes")
        tabla = ttk.Treeview(
            contenedor,
            columns=columnas,
            show="headings",
            style="Club.Treeview",
            height=12,
            selectmode="browse",
        )
        tabla.heading("usuario", text="Usuario", anchor="w")
        tabla.heading("nombre", text="Nombre", anchor="w")
        tabla.heading("estado", text="Estado")
        tabla.heading("inscripcion", text="Inscripción")
        tabla.heading("pendientes", text="Cuotas pendientes")
        tabla.column("usuario", width=130, anchor="w")
        tabla.column("nombre", width=220, anchor="w")
        tabla.column("estado", width=110, anchor="center")
        tabla.column("inscripcion", width=130, anchor="center")
        tabla.column("pendientes", width=140, anchor="center")

        # Un solo tag por fila: activos con rayado azul suave,
        # suspendidos con fondo rosado y texto rojo.
        tabla.tag_configure("par", background=FILA_PAR, foreground=TEXTO)
        tabla.tag_configure("impar", background=PANEL, foreground=TEXTO)
        tabla.tag_configure("susp_par", background=FILA_SUSPENDIDO_PAR,
                            foreground=ESTADO_SUSPENDIDO)
        tabla.tag_configure("susp_impar", background=FILA_SUSPENDIDO,
                            foreground=ESTADO_SUSPENDIDO)

        barra = ttk.Scrollbar(contenedor, orient="vertical",
                              command=tabla.yview,
                              style="Club.Vertical.TScrollbar")
        tabla.configure(yscrollcommand=barra.set)
        barra.pack(side="right", fill="y")
        tabla.pack(side="left", fill="both", expand=True)

        fila_botones = tk.Frame(self, bg=PANEL)
        fila_botones.pack(pady=(0, 16))

        self._crear_boton_accion(
            fila_botones,
            "SUSPENDER",
            lambda: self._cambiar_estado(tabla, suspender_socio),
            ESTADO_SUSPENDIDO,
            ESTADO_SUSPENDIDO_HOVER,
        ).pack(side="left", padx=8)

        self._crear_boton_accion(
            fila_botones,
            "REACTIVAR",
            lambda: self._cambiar_estado(tabla, reactivar_socio),
            ESTADO_ACTIVO,
            ESTADO_ACTIVO_HOVER,
        ).pack(side="left", padx=8)

        self._cargar_socios(tabla)

    def _cargar_socios(self, tabla):
        for fila in tabla.get_children():
            tabla.delete(fila)
        self._usuarios = []

        socios = listar_socios()

        if not socios:
            tk.Label(
                self,
                text="No hay socios registrados",
                font=FUENTE,
                bg=PANEL,
                fg=TEXTO_SUAVE,
            ).pack(pady=10)
            return

        for indice, socio in enumerate(socios):
            pendientes = [
                cuota for cuota in listar_cuotas(socio.get_usuario())
                if cuota.get_estado() in ("Pendiente", "Vencida")
            ]
            rayado = "par" if indice % 2 == 0 else "impar"
            if socio.estado == "Suspendido":
                rayado = "susp_" + rayado
            tabla.insert(
                "",
                "end",
                values=(
                    socio.get_usuario(),
                    socio.nombre_completo,
                    socio.estado,
                    socio.fecha_inscripcion,
                    len(pendientes),
                ),
                tags=(rayado,),
            )
            self._usuarios.append(socio.get_usuario())

    def _usuario_seleccionado(self, tabla):
        seleccion = tabla.selection()
        if not seleccion or not self._usuarios:
            messagebox.showwarning("Aviso", "Seleccioná un socio primero.")
            return None
        return self._usuarios[tabla.index(seleccion[0])]

    def _cambiar_estado(self, tabla, servicio):
        usuario = self._usuario_seleccionado(tabla)
        if usuario is None:
            return

        mensaje = servicio(usuario)
        messagebox.showinfo("Gestión de socios", mensaje)
        self.mostrar_socios()

    def mostrar_registro(self):
        self._limpiar()
        self._crear_titulo(
            "REGISTRAR NUEVO SOCIO",
            "Los campos marcados con * son obligatorios. "
            "El socio se crea con estado Activo.",
        )

        formulario = tk.Frame(self, bg=PANEL, highlightbackground=BORDE,
                              highlightthickness=1)
        formulario.pack(pady=10, ipadx=30, ipady=14)

        campos = {}
        for fila, (etiqueta, clave, ocultar) in enumerate(CAMPOS_REGISTRO):
            tk.Label(
                formulario,
                text=f"{etiqueta}:",
                font=FUENTE_NEGRITA,
                bg=PANEL,
                fg=TEXTO,
            ).grid(row=fila, column=0, sticky="e", padx=(20, 12), pady=7)

            entrada = tk.Entry(
                formulario,
                font=FUENTE,
                width=28,
                show=ocultar,
                bg=CAMPO,
                fg=TEXTO,
                relief="flat",
                highlightthickness=1,
                highlightbackground=BORDE,
                highlightcolor=PRIMARIO,
                insertbackground=TEXTO,
            )
            entrada.grid(row=fila, column=1, padx=(0, 20), pady=7, ipady=5)
            campos[clave] = entrada

        self.app.crear_boton(
            self,
            "GUARDAR SOCIO",
            lambda: self._guardar(campos),
            ancho=22,
        ).pack(pady=(10, 12))

    def _guardar(self, campos):
        try:
            socio = registrar_socio(
                campos["nombre"].get(),
                campos["edad"].get(),
                campos["tipo_identificacion"].get(),
                campos["identificacion"].get(),
                campos["nacionalidad"].get(),
                date.today(),
                "Activo",
                "socio",
                campos["usuario"].get(),
                campos["contrasenia"].get(),
            )
        except ValueError as error:
            messagebox.showerror("Datos inválidos", str(error))
            return

        messagebox.showinfo(
            "Registrar socio",
            f"El socio '{socio.get_usuario()}' se registró correctamente.",
        )
        self.mostrar_socios()