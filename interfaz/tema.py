from pathlib import Path
# ── Identidad del club ─────────────────────────────────────────
NOMBRE_CLUB = "Nova Esports"
LEMA_CLUB = "Todo tu club en un solo lugar."
SUBTITULO = "Automatiza la rutina, impulsa el deporte."
ETIQUETA = "Socios | Cuotas | Clubes"

# ── Colores ────────────────────────────────────────────────────
PRIMARIO = "#2563EB"
PRIMARIO_HOVER = "#1D4ED8"
PANEL = "#FFFFFF"
FONDO = "#F0F4F8"
TEXTO = "#1E293B"
TEXTO_CLARO = "#FFFFFF"
FILA_PAR = "#E8EEF7"
ESTADO_ACTIVO = "#1E7A1E"
ESTADO_SUSPENDIDO = "#B00020"
ESTADO_VENCIDO = "#B00020"
ESTADO_PENDIENTE = "#B26A00"

# ── Fuentes ────────────────────────────────────────────────────
FUENTE_TITULO = ("Arial", 20, "bold")
FUENTE_GRANDE = ("Arial", 30, "bold")
FUENTE_SUBTITULO = ("Arial", 16, "bold")
FUENTE = ("Arial", 11)
FUENTE_NEGRITA = ("Arial", 11, "bold")
FUENTE_CHICA = ("Arial", 10)
FUENTE_MENU = ("Arial", 11)
FUENTE_TABLA = ("Arial", 10)

#── Logo ───────────────────────────────────────────────────────
# Cada grupo guarda su logo como club/logo.png; si el archivo no
# existe, la interfaz muestra el nombre del club en texto.
RUTA_LOGO = Path(__file__).parent.parent / "club/logo.png"