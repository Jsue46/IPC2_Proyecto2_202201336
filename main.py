import tkinter as tk
from tkinter import Menu
from tkinter import scrolledtext
from tkinter import filedialog
class ventana_principal:
    def __init__(self,root):
        self.root = root
        self.root.title("Proyecto 2")
        self.root.geometry("600x600")
        self.root.resizable(0,0)
        self.root.configure(bg="gray")
        titulo_frame = tk.Frame(self.root, bg="gray")
        label_titulo = tk.Label(titulo_frame, text="Analizador de Maquetas")
        label_titulo.config(font=("Arial", 20), bg="#4A6EB0",fg="white")
        label_titulo.pack(fill="both", expand=True)
        titulo_frame.place(x=0, y=0, )
        titulo_frame.config(width=600, height=50)
        titulo_frame.pack_propagate(0)
        #boton archivo
        opciones_frame = tk.Frame(root, bg="gray")
        boton_archivo = tk.Menubutton(opciones_frame, text="Archivo", bg="#142157", font=("Arial", 12), bd=0, fg="white", activeforeground='black')
        boton_archivo.place(x=50, y=10, width=150, height=50)
        opciones=Menu(boton_archivo, tearoff=0)
        boton_archivo["menu"] = opciones    
        opciones.add_command(label="Abrir", font=("Arial", 12), activeforeground='black', command=self.abrir_archivo)
        opciones.add_command(label="salir", font=("Arial", 12), activeforeground='black', command=self.salir)
        #boton gestion de maquetas
        boton_maquetas = tk.Menubutton(opciones_frame, text="Maquetas", bg="#142157", font=("Arial", 12), bd=0, fg="white", activeforeground='black')
        boton_maquetas.place(x=50, y=75, width=150, height=50)
        opciones=Menu(boton_maquetas, tearoff=0)
        boton_maquetas["menu"] = opciones
        opciones.add_command(label="Cargar", font=("Arial", 12), activeforeground='black')
        opciones.add_command(label="salir", font=("Arial", 12), activeforeground='black',command=self.salir)
        #boton resolucion de maquetas
        boton_resolucion = tk.Menubutton(opciones_frame, text="Resolucion", bg="#142157", font=("Arial", 12), bd=0, fg="white", activeforeground='black')   
        boton_resolucion.place(x=50, y=140, width=150, height=50)
        opciones=Menu(boton_resolucion, tearoff=0)
        boton_resolucion["menu"] = opciones
        opciones.add_command(label="Cargar", font=("Arial", 12), activeforeground='black')
        opciones.add_command(label="salir", font=("Arial", 12), activeforeground='black', command=self.salir)
        #boton ayuda
        boton_ayuda = tk.Menubutton(opciones_frame, text="Ayuda", bg="#142157", font=("Arial", 12), bd=0, fg="white", activeforeground='black') 
        boton_ayuda.place(x=50, y=205, width=150, height=50)
        opciones=Menu(boton_ayuda, tearoff=0)
        boton_ayuda["menu"] = opciones
        opciones.add_command(label="Manual de Usuario", font=("Arial", 12), activeforeground='black')
        opciones.add_command(label="salir", font=("Arial", 12), activeforeground='black', command=self.salir)
        #configuracion de frame
        opciones_frame.place(x=200, y=150)
        opciones_frame.pack_propagate()
        opciones_frame.config(width=1200, height=400)







    def abrir_archivo(self):
        file_path = tk.filedialog.askopenfilename()
        print(file_path)
        
    def salir(self):
        self.root.quit()
        self.root.destroy()
        exit()



if __name__ == "__main__":
    ventana = tk.Tk()
    aplicacion = ventana_principal(ventana)
    ventana.mainloop()