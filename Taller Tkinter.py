import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

def init_window():

    window = tk.Tk()
    window.title('Calculadora')
    window.geometry('725x500')

    def agregar():
        global spin
        spin = tk.Spinbox(window, from_=0, to= 100,width=20)
        spin.grid(column= 1, row= 4)

    def seguir():
        global spin
        spin = tk.Spinbox(window, values= 0)
        spin.grid(column=1, row= 4)

    label = tk.Label(window, text='Calculadora', font=('Arial bold', 25))
    label.grid(column = 0, row = 0)

    entrada1 = tk.Entry(window, width=40)
    entrada2 = tk.Entry(window, width=40)

    entrada1.grid(column = 1, row = 1, columnspan=2)
    entrada2.grid(column = 1, row = 2, columnspan=2)


    label_entrada1 = tk.Label(window, text = 'Ingrese primer número:', font=('Arial bold', 20))
    label_entrada1.grid(column = 0, row = 1)

    label_entrada2 = tk.Label(window, text = 'Ingrese segundo número:', font=('Arial bold', 20))
    label_entrada2.grid(column = 0, row= 2)

    label_rad2 = tk.Label(window, text='Si no quiere agregar número seleccione continuar', font=('Arial bold',12))
    label_rad2.grid(column=1,row=5, columnspan=2)

    rad1 = Radiobutton(window, text = 'Agregar otro número', value = 1, command= agregar)
    rad1.grid(column = 1, row= 3)

    rad2 = Radiobutton(window, text = 'Continuar', value =2, command= seguir)
    rad2.grid(column= 2, row=3)

    label_operador = tk.Label(window,text = 'Escoja un operador', font =('Arial bold', 20))
    label_operador.grid(column= 0, row= 6)

    combo_operadores = ttk.Combobox(window)
    combo_operadores['values'] = ['+','-','*','/','pow']
    combo_operadores.current(0)
    combo_operadores.grid(column = 1, row= 6)

    label_resultado = tk.Label(window, text='Resultado: ', font=('Arial bold', 25))
    label_resultado.grid(column = 0, row = 9)


    boton = tk.Button(window,
                      command=lambda: click_calcular(
                          label_resultado,
                          entrada1.get(),
                          entrada2.get(),
                          combo_operadores.get(),
                          spin.get()),
                      text='Calcular',
                      bg='purple',
                      fg='white')
    boton.grid(column=1, row=8)

    label_binario= tk.Label(text='Seleccine la opcion binario para ver el resultado en base 2', font=('Arial bold',14))
    label_binario.grid(column=0, row= 10, columnspan=2)

    chk_state = BooleanVar()
    chk_state.set(False)
    chk = Checkbutton(window,
                    command=lambda:  binario(
                        label_resultado2,
                        res),
                    text='Binario',
                    var=chk_state)
    chk.grid(column=2, row=10, columnspan=2)

    label_resultado2 = tk.Label(window, text='Resultado en binario: ', font=('Arial bold', 25))
    label_resultado2.grid(column=0, row=11, columnspan=2)

    def binario(label, s):
        s = int(s)
        n = ''
        f = 0
        while s != 0:
            f = s % 2
            n = n+str(f)
            s = s // 2
            respuesta = n[::-1]
            label.configure(text='Resultado en binario: ' + str(respuesta))

    window.mainloop()


def calculadora (num1, num2 ,num3, operador):

    if operador == '+':
        resultado = num1 + num2 + num3
    elif operador == '-':
        resultado = num1 - num2 - num3
    elif operador == '*':
        if num3 == 0:
            num3 = 1
        resultado = num1 * num2 * num3
    elif operador == '/':
        if num3 == 0:
            num3 = 1
        resultado = round((num1 / num2) /num3, 2)
    else:
        if num3 == 0:
            num3 = 1
        resultado = (num1 ** num2) ** num3
    return resultado

def click_calcular(label, num1, num2, operador, num3= 0):
    valor1 = float(num1)
    valor2 = float(num2)
    valor3 = float(num3)
    global res
    res = calculadora(valor1, valor2, valor3, operador)
    label.configure(text = 'Resultado: ' + str(res))

def main():
    init_window()

main()