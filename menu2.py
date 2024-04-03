# LIBRERIAS PYTHON

from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
import os
from graphviz import Digraph
class NodoResultado:

    def __init__(self, valor):
        self.anterior = None
        self.siguiente = None
        self.valor = valor
class NodoPosicion:

    def __init__(self, valor):
        self.anterior = None
        self.siguiente = None
        self.valor = valor
class NodoObjetivo:

    def __init__(self, valor):
        self.anterior = None
        self.siguiente = None
        self.valor = valor
class NodoMaqueta:

    def __init__(self, valor):
        self.anterior = None
        self.siguiente = None
        self.valor = valor
class NodoEstructura:

    def __init__(self, valor):
        self.anterior = None
        self.siguiente = None
        self.valor = valor
class NodoEntrada:

    def __init__(self, valor):
        self.anterior = None
        self.siguiente = None
        self.valorEntrada = valor
class ClaseEntrada:

    def __init__(self, filaEntrada, columnaEntrada):
        self.filaEntrada = filaEntrada
        self.columnaEntrada = columnaEntrada

class ClaseMaqueta:

    def __init__ (self, nombreMaqueta, filaMaqueta, columnaMaqueta, entradaMaqueta, objetivosMaqueta, estructuraMaqueta):
        self.nombreMaqueta = nombreMaqueta
        self.filaMaqueta = filaMaqueta
        self.columnaMaqueta = columnaMaqueta
        self.entradaMaqueta = entradaMaqueta
        self.objetivosMaqueta = objetivosMaqueta
        self.estructuraMaqueta = estructuraMaqueta

class ClaseObjetivo:

    def __init__(self, nombreObjetivo, filaObjetivo, columnaObjetivo):
        self.nombreObjetivo = nombreObjetivo
        self.filaObjetivo = filaObjetivo
        self.columnaObjetivo = columnaObjetivo

class ClasePosicion:

    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna

class ListaEntradas:

    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertarEntrada(self, nodoEntrada):
        
        if self.cabeza == None:
            self.cabeza = nodoEntrada
            self.cola = nodoEntrada
        else:
            nodoEntrada.anterior = self.cola
            self.cola.siguiente = nodoEntrada
            self.cola = nodoEntrada

class ListaEstructura:

    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertarEstructura(self, nodoEstructura):
        
        if self.cabeza == None:
            self.cabeza = nodoEstructura
            self.cola = nodoEstructura
        else:
            nodoEstructura.anterior = self.cola
            self.cola.siguiente = nodoEstructura
            self.cola = nodoEstructura

    def imprimeEstructura(self, columna):
        tmpNodoActual = self.cabeza

        i = 0
        fila = ""
        while tmpNodoActual:
            i += 1
            fila += f"|{tmpNodoActual.valor}|"
            if i == int(columna):
                print(fila)
                fila = ""
                i = 0
            tmpNodoActual = tmpNodoActual.siguiente



class ListaMaquetas:

    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertarMaqueta(self, nodoMaqueta):
        
        if self.cabeza == None:
            self.cabeza = nodoMaqueta
            self.cola = nodoMaqueta
        else:
            nodoMaqueta.anterior = self.cola
            self.cola.siguiente = nodoMaqueta
            self.cola = nodoMaqueta

    def ordenarMaquetas(self):
        if self.cabeza == None:
            return
        
        tmpNodo1 = self.cabeza.siguiente

        while tmpNodo1:
            tmpValor = tmpNodo1.valor
            tmpNodoAnterior = tmpNodo1.anterior

            while tmpNodoAnterior != None and tmpNodoAnterior.valor.nombreMaqueta > tmpValor.nombreMaqueta:
                tmpNodoAnterior.siguiente.valor = tmpNodoAnterior.valor
                tmpNodoAnterior = tmpNodoAnterior.anterior

            if tmpNodoAnterior == None:
                self.cabeza.valor = tmpValor
            else:
                tmpNodoAnterior.siguiente.valor = tmpValor

            tmpNodo1 = tmpNodo1.siguiente

        return
    

    def imprimirMaquetas(self):
        tmpNodoActual = self.cabeza

        while tmpNodoActual:
            print("-------------------------------------------------")
            print(f"Nombre Maqueta: {tmpNodoActual.valor.nombreMaqueta}")
            print(f"Nro de filas: {tmpNodoActual.valor.filaMaqueta}")
            print(f"Nro de columnas: {tmpNodoActual.valor.columnaMaqueta}")
            print(f"Entrada de la maqueta: {tmpNodoActual.valor.entradaMaqueta.filaEntrada}x{tmpNodoActual.valor.entradaMaqueta.columnaEntrada}")
            print("     OBJETIVOS---------------------")
            tmpNodoActual.valor.objetivosMaqueta.imprimeObjetivos()
            tmpNodoActual.valor.estructuraMaqueta.imprimeEstructura(tmpNodoActual.valor.columnaMaqueta)
            tmpNodoActual = tmpNodoActual.siguiente
        return
    
    def existePosicion(self, listaPosiciones, posicion):
        tmpListaPosiciones = listaPosiciones.cabeza

        while tmpListaPosiciones:
            if int(tmpListaPosiciones.valor.fila) == int(posicion.fila) and int(tmpListaPosiciones.valor.columna) == int(posicion.columna):
                return True
            tmpListaPosiciones = tmpListaPosiciones.siguiente


    def esObjetivo(self, posX, posY, objetivos):
        tmpObjetivos = objetivos
        while tmpObjetivos:
            if int(tmpObjetivos.valor.filaObjetivo) == int(posY) and int(tmpObjetivos.valor.columnaObjetivo) == int(posX):
                return tmpObjetivos.valor.nombreObjetivo
            
            tmpObjetivos = tmpObjetivos.siguiente
        
        return ""

    
    def validaPosicion(self, sigMovimiento, antMovimiento, Estructura, posX, posY, listaPosiciones, valFila, valColumna, contadorObjetivos, objetivosAlcanzados, objetivos):

        limiteY = valFila
        limiteX = valColumna



        if int(sigMovimiento) == 1: # IZQUIERDA

            tmpEstructura = Estructura.anterior
            if int(posX) == 0 or str(tmpEstructura.valor) == "*" or int(antMovimiento) == 2:
                return False
            
            movimientoX = posX - 1
            movimientoY = posY

            clasePosicion = ClasePosicion(movimientoY, movimientoX)

            # SE VALIDA QUE NO VUELVA HACIA UNA MISMA POSICION
            if self.existePosicion(listaPosiciones, clasePosicion):
                return False
            
            if self.esObjetivo(movimientoX, movimientoY, objetivos) != "":
                objetivosAlcanzados += 1

            nodoPosicion = NodoPosicion(clasePosicion)
            listaPosiciones.insertarPosicion(nodoPosicion)
            nodoMovimiento = NodoPosicion(sigMovimiento)
            listaPosiciones.listaMovimientos.insertarPosicion(nodoMovimiento)
        
        if int(sigMovimiento) == 2: # DERECHA

            tmpEstructura = Estructura.siguiente
            if int(posX) == int(limiteX) - 1 or str(tmpEstructura.valor) == "*" or int(antMovimiento) == 1:
                return False
            
            movimientoX = posX + 1
            movimientoY = posY
            clasePosicion = ClasePosicion(movimientoY, movimientoX)
            # SE VALIDA QUE NO VUELVA HACIA UNA MISMA POSICION
            if self.existePosicion(listaPosiciones, clasePosicion):
                return False
            
            if self.esObjetivo(movimientoX, movimientoY, objetivos) != "":
                objetivosAlcanzados += 1
            
            nodoPosicion = NodoPosicion(clasePosicion)
            listaPosiciones.insertarPosicion(nodoPosicion)
            nodoMovimiento = NodoPosicion(sigMovimiento)
            listaPosiciones.listaMovimientos.insertarPosicion(nodoMovimiento)

        if int(sigMovimiento) == 3: # ABAJO
            
            if int(posY) >= int(limiteY) - 1 or int(antMovimiento) == 4:
                return False


            tmpEstructura = Estructura
            n = 0
            while n != int(limiteX):
                tmpEstructura = tmpEstructura.siguiente
                n += 1
            
            if str(tmpEstructura.valor) == "*":
                return False
            
            movimientoX = posX
            movimientoY = posY + 1
            clasePosicion = ClasePosicion(movimientoY, movimientoX)
            # SE VALIDA QUE NO VUELVA HACIA UNA MISMA POSICION
            if self.existePosicion(listaPosiciones, clasePosicion):
                return False
            
            if self.esObjetivo(movimientoX, movimientoY, objetivos) != "":
                objetivosAlcanzados += 1
            
            nodoPosicion = NodoPosicion(clasePosicion)
            listaPosiciones.insertarPosicion(nodoPosicion)
            nodoMovimiento = NodoPosicion(sigMovimiento)
            listaPosiciones.listaMovimientos.insertarPosicion(nodoMovimiento)

        if int(sigMovimiento) == 4: # ARRIBA
            
            if int(posY) == 0 or int(antMovimiento) == 3:
                return False


            tmpEstructura = Estructura
            n = 0
            while n != int(limiteX):
                tmpEstructura = tmpEstructura.anterior
                n += 1

            if str(tmpEstructura.valor) == "*":
                return False
            
            movimientoX = posX
            movimientoY = posY - 1
            clasePosicion = ClasePosicion(movimientoY, movimientoX)
            # SE VALIDA QUE NO VUELVA HACIA UNA MISMA POSICION
            if self.existePosicion(listaPosiciones, clasePosicion):
                return False
            
            if self.esObjetivo(movimientoX, movimientoY, objetivos) != "":
                objetivosAlcanzados += 1

            nodoPosicion = NodoPosicion(clasePosicion)
            listaPosiciones.insertarPosicion(nodoPosicion)
            nodoMovimiento = NodoPosicion(sigMovimiento)
            listaPosiciones.listaMovimientos.insertarPosicion(nodoMovimiento)

        if self.buscarPosiciones(tmpEstructura, movimientoX, movimientoY, listaPosiciones, limiteY, limiteX, contadorObjetivos, objetivosAlcanzados, objetivos):
            return True


    def buscarPosiciones(self, tmpEstructura, posX, posY, listaPosiciones, valFila, valColumna, contadorObjetivos, objetivosAlcanzados, objetivos):
        if contadorObjetivos == objetivosAlcanzados:
            return True
        
        # SE VALIDA MOVIMIENTO HACIA LA IZQUIERDA
        if(self.validaPosicion(1, listaPosiciones.listaMovimientos.cola.valor, tmpEstructura, posX, posY, listaPosiciones, valFila, valColumna, contadorObjetivos, objetivosAlcanzados, objetivos)):
            return True
        # SE VALIDA MOVIMIENTO HACIA LA DERECHA
        if(self.validaPosicion(2, listaPosiciones.listaMovimientos.cola.valor, tmpEstructura, posX, posY, listaPosiciones, valFila, valColumna, contadorObjetivos, objetivosAlcanzados, objetivos)):
            return True
        # SE VALIDA MOVIMIENTO HACIA ABAJO
        if(self.validaPosicion(3, listaPosiciones.listaMovimientos.cola.valor, tmpEstructura, posX, posY, listaPosiciones, valFila, valColumna, contadorObjetivos, objetivosAlcanzados, objetivos)):
            return True
        # SE VALIDA MOVIMIENTO HACIA ARRIBA
        if(self.validaPosicion(4, listaPosiciones.listaMovimientos.cola.valor, tmpEstructura, posX, posY, listaPosiciones, valFila, valColumna, contadorObjetivos, objetivosAlcanzados, objetivos)):
            return True
        
        listaPosiciones.borrarPosicion()
        listaPosiciones.listaMovimientos.borrarPosicion()

    def resolverMaqueta(self, selMaqueta):
        if selMaqueta == "":
            messagebox.showerror("Error", "Por favor, seleccione una maqueta")
            return
        
        print(f"Maqueta seleccionada: {selMaqueta}")

        maqueta = self.cabeza

        while maqueta:
            if maqueta.valor.nombreMaqueta == selMaqueta:
                break
            maqueta = maqueta.siguiente

        if maqueta is None:
            messagebox.showerror("Error", "No se encontró la maqueta, vuelve a seleccionarlo")
            return
        
        filaInicio = maqueta.valor.entradaMaqueta.filaEntrada
        columnaInicio = maqueta.valor.entradaMaqueta.columnaEntrada
        valFila = maqueta.valor.filaMaqueta
        valColumna = maqueta.valor.columnaMaqueta

        # ENCONTRAMOS EL PUNTO DE INICIO
        tmpEstructura = maqueta.valor.estructuraMaqueta.cabeza
        i = 0
        j = 0 
        while tmpEstructura:
            
            if i == int(filaInicio) and j == int(columnaInicio):
                print(f"se encontró inicio en {i}x{j}")
                break

            if j == int(valColumna) - 1:
                i += 1
                j = 0
            else:
                j += 1
            tmpEstructura = tmpEstructura.siguiente


        # CONTADOR DE OBJETIVOS
        tmpObjetivos = maqueta.valor.objetivosMaqueta.cabeza
        contadorObjetivos = 0
        objetivosAlcanzados = 0
        while tmpObjetivos:
            contadorObjetivos += 1
            tmpObjetivos = tmpObjetivos.siguiente

        listaResultados = ListaResultado()
        listaPosiciones = ListaPosiciones()
        listaPosiciones.listaMovimientos = ListaPosiciones()
        nodoMovimiento = NodoPosicion(0)
        listaPosiciones.listaMovimientos.insertarPosicion(nodoMovimiento)
        self.buscarPosiciones(tmpEstructura, j, i, listaPosiciones, valFila, valColumna, contadorObjetivos, objetivosAlcanzados, maqueta.valor.objetivosMaqueta.cabeza)
        if listaPosiciones.cabeza == None:
            messagebox.showerror("Error", "Maqueta no tiene solución")

        self.imprimirMaqueta(maqueta.valor.nombreMaqueta, listaPosiciones)

    def imprimirMaqueta(self, nombre, listaPosiciones):
        tmpMaqueta = self.cabeza
        while tmpMaqueta:
            if str(tmpMaqueta.valor.nombreMaqueta) == nombre:
                break

            tmpMaqueta = tmpMaqueta.siguiente

        if tmpMaqueta is None:
            messagebox.showerror("Error", "No existe maqueta seleccionada")
            return False
        
        if listaPosiciones is None:
            listaPosiciones = ListaPosiciones()
        
        dot = Digraph('G')
        dot.attr(rankdir='LR')
        dot.attr('node', shape='box', style='filled')

        filas = int(tmpMaqueta.valor.filaMaqueta)
        columnas = int(tmpMaqueta.valor.columnaMaqueta)

        tmpEstructura = tmpMaqueta.valor.estructuraMaqueta.cola

        with dot.subgraph(name='matriz_laberinto') as c:

            for i in range(filas):
                for j in range(columnas):

                    idNodo = node_id = f'{str(filas - i) + str(columnas - j)}'
                    
                    if tmpEstructura is None:
                        break

                    if str(tmpEstructura.valor) == "*":
                        c.node(f'{idNodo}', label="", fillcolor='black', fontcolor='white')
                    else:
                        colorCamino = 'white'
                        if self.existePosicion(listaPosiciones, ClasePosicion(filas - i - 1, columnas - j - 1)):
                            colorCamino = 'green'
                        
                        nombreLbl = self.esObjetivo(columnas - j - 1, filas - i - 1, tmpMaqueta.valor.objetivosMaqueta.cabeza)
                        if int(tmpMaqueta.valor.entradaMaqueta.filaEntrada) == int(filas - i - 1) and int(tmpMaqueta.valor.entradaMaqueta.columnaEntrada) == int(columnas - j - 1):
                            nombreLbl = "X"
                            colorCamino = 'green'
                        
                        c.node(f'{idNodo}', fillcolor=colorCamino, label=f"{nombreLbl}")
                    
                    if j > 0:
                        c.edge(f'{idNodo}', f'{idNodo}', style='invis')
                    if i > 0:
                        c.edge(f'{idNodo}', f'{idNodo}', style='invis')
                    
                    tmpEstructura = tmpEstructura.anterior

        tmpEstructura = tmpMaqueta.valor.estructuraMaqueta.cabeza

        for i in range(filas):
            tmpFilaA = ''
            tmpFilaB = ''
            tmpEdgeNode = []
            for j in range(columnas):
                tmpFilaB = tmpFilaA
                tmpFilaA = f'{str(i + 1) + str(j + 1)}'
                if(tmpFilaB != ''):
                    tmpEdgeNode.append((f'{tmpFilaB}', f'{tmpFilaA}'))

            dot.edges(tmpEdgeNode)
            dot.edge_attr.update(style='invis')

        # Configurar la separación entre nodos
        dot.attr('graph', nodesep='-5', ranksep='-5')

        dot.render(f'Maqueta_{tmpMaqueta.valor.nombreMaqueta}.gv', view=True)


class ListaObjetivos:

    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertarObjetivo(self, nodoObjetivo):
        
        if self.cabeza == None:
            self.cabeza = nodoObjetivo
            self.cola = nodoObjetivo
        else:
            nodoObjetivo.anterior = self.cola
            self.cola.siguiente = nodoObjetivo
            self.cola = nodoObjetivo

    def imprimeObjetivos(self):
        tmpNodoActual = self.cabeza
        while tmpNodoActual:
            print(f"     Nombre objetivo: {tmpNodoActual.valor.nombreObjetivo} | Posición: {tmpNodoActual.valor.filaObjetivo}x{tmpNodoActual.valor.columnaObjetivo}")
            tmpNodoActual = tmpNodoActual.siguiente
        return
    
class ListaPosiciones:

    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.movimientos = 0
        self.listaMovimientos = None

    def insertarPosicion(self, nodoPosicion):
        
        if self.cabeza == None:
            self.cabeza = nodoPosicion
            self.cola = nodoPosicion
        else:
            nodoPosicion.anterior = self.cola
            self.cola.siguiente = nodoPosicion
            self.cola = nodoPosicion

    def borrarPosicion(self):
        if self.cabeza == None:
            return
        
        if self.cabeza.siguiente == None:
            self.cabeza = None
        else:
            actual = self.cabeza
            while actual.siguiente.siguiente:
                actual = actual.siguiente
            actual.siguiente = None
            self.cola = actual

    def imprimeEstructura(self, columna):
        tmpNodoActual = self.cabeza

        i = 0
        fila = ""
        while tmpNodoActual:
            i += 1
            fila += f"|{tmpNodoActual.valor}|"
            if i == int(columna):
                print(fila)
                fila = ""
                i = 0
            tmpNodoActual = tmpNodoActual.siguiente

class ListaResultado:

    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertarResultado(self, nodoEstructura):
        
        if self.cabeza == None:
            self.cabeza = nodoEstructura
            self.cola = nodoEstructura
        else:
            nodoEstructura.anterior = self.cola
            self.cola.siguiente = nodoEstructura
            self.cola = nodoEstructura

    def imprimeEstructura(self, columna):
        tmpNodoActual = self.cabeza

        i = 0
        fila = ""
        while tmpNodoActual:
            i += 1
            fila += f"|{tmpNodoActual.valor}|"
            if i == int(columna):
                print(fila)
                fila = ""
                i = 0
            tmpNodoActual = tmpNodoActual.siguiente



def lectorXML(listaMaquetas):
    urlArchivo = filedialog.askopenfile(filetype=[('XML files', '*.xml')])
    if not urlArchivo:
        print("Fallo an intentar cargar el archivo, vuelve a intentarlo")
        return
    
    listaMaquetas.cabeza = None
    listaMaquetas.cola = None
    xml = minidom.parse(urlArchivo)
    maquetas = xml.getElementsByTagName('maqueta')

    for i in maquetas:
        print(i.getElementsByTagName('nombre')[0].firstChild.data)
        print(i.getElementsByTagName('filas')[0].firstChild.data)
        print(i.getElementsByTagName('columnas')[0].firstChild.data)
        print(i.getElementsByTagName('estructura')[0].firstChild.data)
        entrada = ClaseEntrada(i.getElementsByTagName('fila')[0].firstChild.data, 
                               i.getElementsByTagName('columna')[0].firstChild.data)
        print(entrada.filaEntrada)
        print(entrada.columnaEntrada)
        listaObjetivos = ListaObjetivos()
        objetivos = i.getElementsByTagName('objetivos')[0].getElementsByTagName('objetivo')
        for objetivo in objetivos:
            print(objetivo.getElementsByTagName('nombre')[0].firstChild.data)
            print(objetivo.getElementsByTagName('fila')[0].firstChild.data)
            print(objetivo.getElementsByTagName('columna')[0].firstChild.data)
            claseObjetivo = ClaseObjetivo(objetivo.getElementsByTagName('nombre')[0].firstChild.data,
                                          objetivo.getElementsByTagName('fila')[0].firstChild.data,
                                          objetivo.getElementsByTagName('columna')[0].firstChild.data)
            nodoObjetivo = NodoObjetivo(claseObjetivo)
            listaObjetivos.insertarObjetivo(nodoObjetivo)
        
        estructura = i.getElementsByTagName('estructura')[0].firstChild.data
        listaEstructura = ListaEstructura()
        for j in estructura:
            if j == ' ':
                continue
            nodoEstructura = NodoEstructura(j)
            listaEstructura.insertarEstructura(nodoEstructura)

        claseMaqueta = ClaseMaqueta(i.getElementsByTagName('nombre')[0].firstChild.data,
                                    i.getElementsByTagName('filas')[0].firstChild.data,
                                    i.getElementsByTagName('columnas')[0].firstChild.data,
                                    entrada,
                                    listaObjetivos,
                                    listaEstructura)
        
        nodoMaqueta = NodoMaqueta(claseMaqueta)
        listaMaquetas.insertarMaqueta(nodoMaqueta)

        print("------------------------------\n\n")
    
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
    os.system("start ./Documentacion/Documentacion_Proyecto2.pdf")

def ventanaAyuda():
    ayuda = tk.Tk()
    ayuda.geometry("500x500")
    ayuda.title("Informacion Proyecto 2")
    ayuda.configure(bg="gray")

    
    nombre = tk.Label(ayuda, text="Estuardo Josué Vaquiax Reyes")
    nombre.config(font=("Arial", 20),bg="gray", fg="white")
    nombre.place(x=0, y=50, width=500, height=50)
    

    carnet = tk.Label(ayuda, text="Carnet: 202201336")
    carnet.config(font=("Arial", 20),bg="gray", fg="white")
    carnet.place(x=0, y=200, width=500, height=50)

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
