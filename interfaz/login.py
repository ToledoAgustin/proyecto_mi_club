import tkinter as tk

ventana = tk.Tk()
ventana.title('App Mi Club')
ventana.geometry("394x749")
ventana.configure(bg="#ffffff")

blanco = "#ffffff"

etiqueta = tk.Label(ventana, text="Ingresa el nombre", bg="#ffffff", fg="#6B7280", font=("Arial", 10, "bold"))
etiqueta.pack(pady=(30, 5))

entrada = tk.Entry(ventana, bg="#F9FAFB", fg="#111827", bd=1, relief="solid", font=("Arial", 10))
entrada.pack(ipady=4, pady=10)


def saludar():
    nombre = entrada.get()
    etiqueta_saludo.config(text=f'Hola {nombre} Saludos')


boton = tk.Button(
    ventana, 
    text="Saludar", 
    bg="#2B4C7E", 
    fg="white", 
    activebackground="#1E3456", 
    activeforeground="white", 
    bd=0, 
    relief="flat", 
    font=("Arial", 10, "bold"), 
    cursor="hand2", 
    command=saludar
)
boton.pack(ipady=5, ipadx=15, pady=15)

etiqueta_saludo = tk.Label(ventana, bg=blanco, fg="#2B4C7E", font=("Arial", 10, "bold"))
etiqueta_saludo.pack(pady=10)

ventana.mainloop()