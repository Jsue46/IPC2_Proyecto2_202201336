from tkinter import filedialog
import tkinter as tk
import os
import xml.etree.ElementTree as ET
###################################################
from clases import ClaseMaqueta, ClaseEntrada, ClaseObjetivo
from nodos import NodoMaqueta, NodoObjetivo, NodoEstructura
from listas import ListaMaquetas, ListaObjetivos, ListaEstructura



def lectorXML(listaMaquetas):
    urlArchivo = filedialog.askopenfilename(filetypes=[('XML files', '*.xml')])
    if not urlArchivo:
        print("Fallo al intentar cargar el archivo, vuelve a intentarlo")
        return

    tree = ET.parse(urlArchivo)
    root = tree.getroot()

    for maqueta in root.findall('.//maqueta'):
        nombre = maqueta.find('nombre').text
        filas = maqueta.find('filas').text
        columnas = maqueta.find('columnas').text
        entrada_fila = maqueta.find('entrada/fila').text
        entrada_columna = maqueta.find('entrada/columna').text

        entrada = ClaseEntrada(entrada_fila, entrada_columna)

        listaObjetivos = ListaObjetivos()
        for objetivo in maqueta.findall('.//objetivo'):
            nombre_objetivo = objetivo.find('nombre').text
            fila_objetivo = objetivo.find('fila').text
            columna_objetivo = objetivo.find('columna').text
            claseObjetivo = ClaseObjetivo(nombre_objetivo, fila_objetivo, columna_objetivo)
            nodoObjetivo = NodoObjetivo(claseObjetivo)
            listaObjetivos.insertarObjetivo(nodoObjetivo)

        estructura = maqueta.find('estructura').text
        listaEstructura = ListaEstructura()
        for char in estructura:
            if char == ' ':
                continue
            nodoEstructura = NodoEstructura(char)
            listaEstructura.insertarEstructura(nodoEstructura)

        claseMaqueta = ClaseMaqueta(nombre, filas, columnas, entrada, listaObjetivos, listaEstructura)

        nodoMaqueta = NodoMaqueta(claseMaqueta)
        listaMaquetas.insertarMaqueta(nodoMaqueta)

    listaMaquetas.ordenarMaquetas()
    listaMaquetas.imprimirMaquetas()




def seleccionMaqueta(listaMaqueta):
    window = tk.Tk()
    window.geometry("500x500")
    window.title("Maquetas")
    window.configure(bg="gray")
    titulomaqueta = tk.Label(window, text="Seleccione una opción a realizar", font=("Helvetica", 25), bg="gray", fg="white")
    
    titulomaqueta.config(font=("Arial", 20), bg="#4A6EB0", fg="white")
    titulomaqueta.pack(fill="both", expand=True)
    titulomaqueta.pack(pady=(0, 0))
    titulomaqueta.place(x=0, y=0, width=500, height=50)
    listbox = tk.Listbox(window)
    listbox.pack(padx=10, pady=150)
    listbox.config(bg="gray", fg="white", font=("Arial", 15))
    
   
   
    tmpListaMaquetas = listaMaqueta.cabeza
    i = 0
    while tmpListaMaquetas:
        listbox.insert(i, f"{tmpListaMaquetas.valor.nombreMaqueta}")
        i += 1
        tmpListaMaquetas = tmpListaMaquetas.siguiente

    listbox.pack()

    boton_imprimir = tk.Button(window, text="Graficar Laberinto", command= lambda: listaMaqueta.imprimirMaqueta(listbox.get(listbox.curselection()), None), bg="#142157", fg="white")
    boton_imprimir.pack()
    boton_imprimir.place(x=125, y=100, width=100, height=50)


    boton_resolver = tk.Button(window, text="Solución", command= lambda: listaMaqueta.resolverMaqueta(listbox.get(listbox.curselection())), bg="#142157", fg="white")
    boton_resolver.pack()
    boton_resolver.place(x=275, y=100, width=100, height=50)
    window.mainloop()  

def abrirDocumentación():
    ruta_carpeta = r"C:\Users\familia\OneDrive\Escritorio\Ingenieria\IPC2\IPC2_Proyecto2_202201336\IPC2_Proyecto2_202201336"
    os.system("start " + ruta_carpeta)

def ventanaAyuda():
    ayuda = tk.Tk()
    ayuda.geometry("500x500")
    ayuda.title("Informacion Proyecto 2")
    ayuda.configure(bg="gray")

    
    nombre = tk.Button(ayuda, text="Estuardo Josué Vaquiax Reyes")
    nombre.config(font=("Arial", 20),bg="#142157", fg="white")
    nombre.place(x=40, y=50, width=400, height=50)
    

    carnet = tk.Button(ayuda, text="Carnet: 202201336")
    carnet.config(font=("Arial", 20),bg="#142157", fg="white")
    carnet.place(x=120, y=200, width=250, height=50)

    boton_resolver = tk.Button(ayuda, text="Documentación", command= lambda: abrirDocumentación())
    boton_resolver.config(font=("Arial", 20),bg="#142157", fg="white")
    boton_resolver.place(x=150, y=400, width=200, height=50)

    ayuda.mainloop()  




###################################################








def main():
    listaMaquetas = ListaMaquetas()
    root = tk.Tk()
    root.geometry("500x500")
    root.title("202201336-Proyecto2")
    root.configure(bg="gray")

    # Agregar un título
    titulo = tk.Label(root, text="Analizador de maquetas", font=("Helvetica", 25), bg="gray", fg="white")
    titulo.config(font=("Arial", 20), bg="#4A6EB0", fg="white")
    titulo.pack(fill="both", expand=True)
    titulo.pack(pady=(0, 60))

    btnCargaArchivo = tk.Button(root, text="Cargar Archivo", width=40, height=5, command=lambda: lectorXML(listaMaquetas), bg="#142157", fg="white")
    btnCargaArchivo.pack(pady=(0, 30))

    btnSeleccionMaqueta = tk.Button(root, text="Seleccionar Maqueta", width=40, height=5, command=lambda: seleccionMaqueta(listaMaquetas), bg="#142157", fg="white")
    btnSeleccionMaqueta.pack(pady=(0, 30))

    btnAyuda = tk.Button(root, text="Ayuda", width=40, height=5, command=lambda: ventanaAyuda(), bg="#142157", fg="white")
    btnAyuda.pack(pady=(0, 30))

    root.mainloop()

if __name__ == "__main__":

    main()
