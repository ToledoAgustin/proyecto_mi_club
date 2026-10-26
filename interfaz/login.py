import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title('App Mi Club - Nova Esports')
ventana.geometry("394x600")

# Paleta de colores claros y cremita
blanco_cremita = "#FAF7F2"          # Blanco cremita suave para el fondo
blanco_puro = "#FFFFFF"         # Blanco puro para las cajas de texto
marron_oscuro = "#3A332C" # Marrón oscuro elegante para los títulos
gris_calido = "#8C827A"      # Gris cálido suave para las etiquetas
beige = "#C49A6C"     # Tono crema/beige tostado para el botón
hover_oscuro = "#B3895B"     # Tono ligeramente más oscuro al presionar el botón

ventana.configure(bg=blanco_cremita)

ventana.configure(bg=blanco_cremita)

# --- Encabezado ---
etiqueta_marca = tk.Label(
    ventana, 
    text="Nova Esports", 
    bg=blanco_cremita, 
    fg=beige, 
    font=("Arial", 11, "bold")
)
etiqueta_marca.pack(pady=(40, 5)) # Posiciona el widget con 40px de margen arriba y 5px abajo

etiqueta_titulo = tk.Label(
    ventana, 
    text="Iniciar Sesión", 
    bg=blanco_cremita, 
    fg=gris_calido, 
    font=("Arial", 20, "bold")
)
etiqueta_titulo.pack(pady=(0, 25)) # Margen vertical: 0px arriba, 25px abajo

# --- Campo Usuario ---
etiqueta_usuario = tk.Label(
    ventana, 
    text="Usuario / Email", 
    bg=blanco_cremita, 
    fg=gris_calido, 
    font=("Arial", 10, "bold")
)
etiqueta_usuario.pack(anchor="w", padx=45, pady=(5, 5)) # Alinea al oeste (izquierda) con sangrado de 45px

entrada_usuario = tk.Entry(
    ventana, 
    bg=blanco_puro,            
    fg=marron_oscuro,          
    bd=1,                      
    relief="solid",            # Estilo del borde con línea continua fina
    font=("Arial", 11)         
)
entrada_usuario.pack(fill="x", padx=45, ipady=6, pady=(0, 15)) # Se estira a lo ancho (fill="x") y le da altura interna (ipady=6)

# --- Campo Contraseña ---
etiqueta_clave = tk.Label(
    ventana, 
    text="Contraseña",         # Texto explicativo para el campo contraseña
    bg=blanco_cremita,         
    fg=gris_calido,           
    font=("Arial", 10, "bold") 
)
etiqueta_clave.pack(anchor="w", padx=45, pady=(5, 5)) # Alineación a la izquierda con margen horizontal

entrada_clave = tk.Entry(
    ventana, 
    bg=blanco_puro,            
    fg=marron_oscuro,          
    show="•",                  # Enmascara los caracteres escritos por viñetas
    bd=1,                      # Borde fino de 1px
    relief="solid",            # Borde sólido
    font=("Arial", 11)         
)
entrada_clave.pack(fill="x", padx=45, ipady=6, pady=(0, 20)) # Ocupa el ancho con padding interno

# --- Lógica del Inicio de Sesión ---
def iniciar_sesion():
    usuario = entrada_usuario.get()  # Lee el texto escrito en la caja de usuario
    clave = entrada_clave.get()      # Lee el texto escrito en la caja de contraseña
    
    if usuario == "" or clave == "": # Evalúa si alguno de los campos quedó vacío
        # Si falta información, muestra una advertencia en rojo (#C0392B)
        etiqueta_mensaje.config(text="Por favor, completa todos los campos", fg="#C0392B")
    else:
        # Si ambos campos tienen texto, confirma el acceso en verde (#27AE60)
        etiqueta_mensaje.config(text=f"¡Bienvenido/a, {usuario}!", fg="#27AE60")

ventana.mainloop()