from nodos import NodoPosicion
from clases import ClasePosiciones
from tkinter import messagebox
from graphviz import Digraph
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

            clasePosicion = ClasePosiciones(movimientoY, movimientoX)

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
            clasePosicion = ClasePosiciones(movimientoY, movimientoX)
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
            clasePosicion = ClasePosiciones(movimientoY, movimientoX)
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
            clasePosicion = ClasePosiciones(movimientoY, movimientoX)
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
        dot.attr('graph', nodesep='0', ranksep='0', margin='0')  # Ajusta los valores según tu preferencia
        dot.attr('node', shape='box', style='filled', width='1', height='1', penwidth='0')  # Ajusta el tamaño de los nodos según tu preferencia

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
                        if self.existePosicion(listaPosiciones, ClasePosiciones(filas - i - 1, columnas - j - 1)):
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

        tmpEdgeNode = Nodo()  # Nodo inicial
        current_edge_node = tmpEdgeNode

        for i in range(filas):
            tmpFilaA = ''
            tmpFilaB = ''
            for j in range(columnas):
                tmpFilaB = tmpFilaA
                tmpFilaA = f'{str(i + 1) + str(j + 1)}'
                if (tmpFilaB != ''):
                    current_edge_node.siguiente = Nodo((f'{tmpFilaB}', f'{tmpFilaA}'))
                    current_edge_node = current_edge_node.siguiente

        edge_node = tmpEdgeNode.siguiente  # Ignorar el primer nodo inicial

        while edge_node:
            dot.edge(edge_node.valor[0], edge_node.valor[1])
            edge_node = edge_node.siguiente

        dot.edge_attr.update(style='invis')

    # Configurar la separación entre nodos y filas
        

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
class Nodo:
    def __init__(self, valor=None):
        self.valor = valor
        self.siguiente = None

        
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
    
    def agregar(self,posicion):
        nuevo_nodo = Nodo(posicion)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            tmp = self.cabeza
            while tmp.siguiente:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo_nodo


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            
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
