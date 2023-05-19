import random
import tkinter as tk
from tkinter import messagebox

import FileReader
from FileReader import *

ventana = tk.Tk()

# variables para llevar el control del juego

palabra_A_Adivinar = ''

userInputs = []

letrasAdivinadas = 0

intentos = 0

advertencias = 3

# Labels para mostrar punajtes, intentos, ...
puntajeActual = tk.Label(ventana, text='y', font=("Arial", 25), bg='teal')

intentosActuales = tk.Label(ventana, text='x', font=("Arial", 25), bg='teal')

#letrasUsadas = tk.Label(ventana, text='a, b, c, ...', font=("Arial", 25), bg='teal')

palabraGuess = tk.Label(ventana, text="palabra", font=("Arial", 25))

# TextBox para ingresar letra y cambiar intentos
inputLetra = tk.Text(ventana, width=3, height=1, font=("Arial", 19))

#inputIntentos = tk.Text(ventana, width=3, height=1, font=("Arial", 19))


def generaVentana():
    # Dimensiones: ancho x alto

    ventana.geometry("1000x500")
    ventana.configure(background="teal")
    ventana.resizable(False, False)  # no permite que se cambien dimensiones de ventana

    tk.Wm.wm_title(ventana, "Ahorcado")
    # posicionando labels dinamicos
    puntajeActual.place(x=180, y=50)
    intentosActuales.place(x=880, y=50)
    #letrasUsadas.place(x=180, y=420)
    palabraGuess.place(x=50, y=193)
    inputLetra.place(x=50, y=250)
    #inputIntentos.place(x=740, y=170)

    generaLabels()
    generaBotones()
    definirArrayPalabras()
    definirPalabra()

    ventana.mainloop()


def generaLabels():
    tk.Label(ventana, text='Puntaje:', font=("Arial", 25), bg='teal').place(x=50, y=50)
    tk.Label(ventana, text="Intentos:", font=("Arial", 25), bg="teal").place(x=750, y=50)
    #tk.Label(ventana, text="Cambiar intentos", font=("Arial", 15), bg="teal").place(x=750, y=100)
    #tk.Label(ventana, text="Letras usadas:", font=("Arial", 25), bg="teal").place(x=50, y=380)


def generaBotones():
    tk.Button(ventana, text='Ingresar letra', font=("Arial", 15), bg='blue', command=cargarLetra).place(x=150, y=250)


def cargarLetra():
    vocales = ['a', 'e', 'i', 'o', 'u']

    global inputLetra, advertencias, intentos
    valor = inputLetra.get("1.0", "end-1c").lower()
    if len(valor) != 1:
        tk.messagebox.showerror(title='Error', message='Ingrese solamente una letra')
    else:

        if not (valor.isalpha()):
            if advertencias != 0:
                advertencias = advertencias - 1
                tk.messagebox.showwarning(title=None,
                                          message='Ingrese una letra\nAdvertencias restantes: ' + str(advertencias))
            else:
                intentos = intentos - 1
                if intentos == 0:
                    tk.messagebox.showerror(title=None,
                                            message='Has perdido, la palabra era: ' + str(palabra_A_Adivinar))
                    reiniciarJuego()
                else:
                    refrescarIntentos()
        elif valor not in palabra_A_Adivinar:
            if valor in vocales:
                intentos = intentos - 2
                refrescarIntentos()
                if intentos <= 0:

                    tk.messagebox.showerror(title=None,
                                            message='Has perdido, la palabra era: ' + str(palabra_A_Adivinar))

                    reiniciarJuego()

            else:
                intentos = intentos - 1
                refrescarIntentos()
                if intentos <= 0:
                    tk.messagebox.showerror(title=None,
                                            message='Has perdido, la palabra era: ' + str(palabra_A_Adivinar))
                    reiniciarJuego()

        else:
            if valor in userInputs:
                if advertencias != 0:
                    advertencias = advertencias - 1
                    tk.messagebox.showwarning(title=None,
                                              message='Letra ya ingresada\nAdvertencias restantes:' + str(advertencias))
                else:
                    intentos = intentos - 1
                    if intentos == 0:
                        tk.messagebox.showerror(title=None,
                                                message='Has perdido, la palabra era: ' + str(palabra_A_Adivinar))
                        reiniciarJuego()
                    else:
                        refrescarIntentos()

            else:
                actualizarString(valor)


def definirPalabra():
    global intentos, palabra_A_Adivinar, userInputs
    indexRandom = random.randint(0, len(FileReader.arrayPalabras))
    palabra_A_Adivinar = FileReader.arrayPalabras[indexRandom]

    for i in range(len(palabra_A_Adivinar)):
        userInputs.append(' ')

    print(palabra_A_Adivinar)
    intentos = 2 * len(palabra_A_Adivinar)
    intentosActuales['text'] = intentos
    puntajeActual['text'] = 0
    # palabraGuess['text'] = palabra_A_Adivinar
    actualizarDisplay()


def actualizarDisplay():
    global letrasAdivinadas, userInputs
    guiones = ''
    palabraGuess['text'] = ''
    letrasAdivinadas = 0
    for i in range(len(palabra_A_Adivinar)):
        if palabra_A_Adivinar[i] != userInputs[i]:
            guiones = guiones + ' _ '
        else:
            guiones = guiones + palabra_A_Adivinar[i]
    countRepetidos()
    palabraGuess['text'] = guiones
    refrescarPunteo()
    stringvalue = ''.join(userInputs)
    if stringvalue == palabra_A_Adivinar:
        tk.messagebox.showinfo(title='Felicidades', message='Haz adivinado la palabra!\n' + 'con un punteo de: ' + str(puntajeActual.cget('text')))
        reiniciarJuego()


def refrescarIntentos():
    intentosActuales['text'] = intentos


def reiniciarJuego():
    global palabra_A_Adivinar, userInputs, letrasAdivinadas, intentos, advertencias

    palabra_A_Adivinar = ''

    userInputs = []

    letrasAdivinadas = 0

    intentos = 0

    advertencias = 3
    definirArrayPalabras()
    definirPalabra()


def refrescarPunteo():
    puntajeActual['text'] = intentos * letrasAdivinadas


def actualizarString(letra):
    global userInputs

    for i in range(len(palabra_A_Adivinar)):
        if letra == palabra_A_Adivinar[i]:
            userInputs[i] = letra
    print(palabra_A_Adivinar)
    print(userInputs)
    actualizarDisplay()


def countRepetidos():
    global letrasAdivinadas
    lista = []
    for letra in userInputs:
        if letra != ' ' and letra not in lista:
            lista.append(letra)
            letrasAdivinadas = letrasAdivinadas + 1
