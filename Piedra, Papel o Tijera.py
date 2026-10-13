import tkinter as tk

root = tk.Tk()
root.title("Piedra, Papel o Tijera")
root.geometry("300x400")

p1, p2 = 0, 0
eleccion1 = ""
turno = 1

def jugar(opcion):
    global eleccion1, turno, p1, p2
    
    if turno == 1:
        eleccion1 = opcion
        lbl_turno.config(text="Turno del Usuario 2")
        turno = 2
    else:
        eleccion2 = opcion
        
        if eleccion1 == eleccion2:
            res = "¡Empate!"
        elif (eleccion1 == "Piedra" and eleccion2 == "Tijera") or \
             (eleccion1 == "Papel" and eleccion2 == "Piedra") or \
             (eleccion1 == "Tijera" and eleccion2 == "Papel"):
            res = "¡Gana Usuario 1!"
            p1 += 1
        else:
            res = "¡Gana Usuario 2!"
            p2 += 1
            
        lbl_res.config(text=f"{res}\nU1: {eleccion1} | U2: {eleccion2}")
        lbl_marcador.config(text=f"Marcador -> U1: {p1}  |  U2: {p2}")
        
        lbl_turno.config(text="¿Jugar otra ronda?")
        btn_p.config(state="disabled")
        btn_pa.config(state="disabled")
        btn_t.config(state="disabled")
        btn_si.pack(pady=5)
        btn_no.pack(pady=5)

def reiniciar(opcion):
    global turno
    if opcion == "si":
        turno = 1
        lbl_res.config(text="")
        lbl_turno.config(text="Turno del Usuario 1")
        btn_p.config(state="normal")
        btn_pa.config(state="normal")
        btn_t.config(state="normal")
        btn_si.pack_forget()
        btn_no.pack_forget()
    else:
        root.destroy()

# Elementos visuales básicos
tk.Label(root, text="Piedra, Papel o Tijera", font=("Arial", 14, "bold")).pack(pady=10)
lbl_marcador = tk.Label(root, text="Marcador -> U1: 0  |  U2: 0", font=("Arial", 11))
lbl_marcador.pack(pady=5)

lbl_turno = tk.Label(root, text="Turno del Usuario 1", font=("Arial", 11, "bold"), fg="blue")
lbl_turno.pack(pady=10)

btn_p = tk.Button(root, text="Piedra", width=15, command=lambda: jugar("Piedra"))
btn_p.pack(pady=3)
btn_pa = tk.Button(root, text="Papel", width=15, command=lambda: jugar("Papel"))
btn_pa.pack(pady=3)
btn_t = tk.Button(root, text="Tijera", width=15, command=lambda: jugar("Tijera"))
btn_t.pack(pady=3)

lbl_res = tk.Label(root, text="", font=("Arial", 10))
lbl_res.pack(pady=10)

btn_si = tk.Button(root, text="Sí", width=10, command=lambda: reiniciar("si"))
btn_no = tk.Button(root, text="No (Salir)", width=10, command=lambda: reiniciar("no"))

root.mainloop()