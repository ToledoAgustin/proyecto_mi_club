from pathlib import Path

# ── Identidad del club ─────────────────────────────────────────
NOMBRE_CLUB = "Nova Esports"
LEMA_CLUB = "Todo tu club en un solo lugar."
SUBTITULO = "Automatiza la rutina, impulsa el deporte."
ETIQUETA = "Socios | Cuotas | Clubes"

# ── Colores ────────────────────────────────────────────────────
PRIMARIO = "#2563EB"           # color principal: encabezado y botones
PRIMARIO_HOVER = "#1D4ED8"     # versión más clara del principal
PANEL = "#FFFFFF"              # fondo del menú lateral y del contenido
FONDO = "#F0F4F8"              # fondo gris detrás de todo
TEXTO = "#1E293B"              # texto oscuro sobre fondos claros
TEXTO_CLARO = "#FFFFFF"        # texto claro sobre el color principal
FILA_PAR = "#E8EEF7"           # rayado suave de las tablas
ESTADO_ACTIVO = "#1E7A1E"      # verde para socios/cuotas activas
ESTADO_SUSPENDIDO = "#B00020"  # rojo para socios suspendidos
ESTADO_VENCIDO = "#B00020"     # rojo para cuotas vencidas
ESTADO_PENDIENTE = "#B26A00"   # naranja para cuotas pendientes

# ── Colores nuevos ────────────────────────────────────
TEXTO_SUAVE = "#64748B"             # texto secundario / subtítulos
BORDE = "#E2E8F0"                   # bordes finos de tarjetas y tablas
ENCABEZADO_TABLA = "#F1F5F9"        # fondo del encabezado de las tablas
FILA_SUSPENDIDO = "#FDECEE"         # fondo rosado para socios suspendidos
FILA_SUSPENDIDO_PAR = "#FADDE1"     # idem, para el rayado
ESTADO_ACTIVO_HOVER = "#166016"     # hover del botón verde
ESTADO_SUSPENDIDO_HOVER = "#8A0019" # hover del botón rojo
CAMPO = "#F8FAFC"                   # fondo de los campos de texto

# ── Fuentes ────────────────────────────────────────────────────
FUENTE_TITULO = ("Arial", 20, "bold")
FUENTE_GRANDE = ("Arial", 30, "bold")
FUENTE_SUBTITULO = ("Arial", 16, "bold")
FUENTE = ("Arial", 11)
FUENTE_NEGRITA = ("Arial", 11, "bold")
FUENTE_CHICA = ("Arial", 10)
FUENTE_MENU = ("Arial", 11)
FUENTE_TABLA = ("Arial", 10)

# ── Logo ───────────────────────────────────────────────────────
# Cada grupo guarda su logo como club/logo.png; si el archivo no
# existe, la interfaz muestra el nombre del club en texto.
RUTA_LOGO = Path(__file__).parent.parent / "logo.png"