#pip install --upgrade googletrans==4.0.0-rc1
from googletrans import Translator
import tkinter

screen = tkinter.Tk()
screen.title("tradutor")
screen.geometry("900x600")
text1 = tkinter.Label(screen,text="digite texto para traducao")
text1.pack()
userInput = tkinter.Entry(screen)
userInput.pack()
traduz = Translator()
def ingles():
    texto = userInput.get()
    resultado = traduz.translate(texto,dest="en")
    result.config(text=resultado.text)
def espanha():
    texto = userInput.get()
    resultado = traduz.translate(texto,dest="es")
    traduzir = resultado.text
    result.config(text=traduzir)
def portugues():
    texto = userInput.get()
    resultado = traduz.translate(texto,dest="pt")
    traduzir = resultado.text
    result.config(text=traduzir)

button1 = tkinter.Button(screen, text="espanhol", command=espanha)
button1.pack()

button2 = tkinter.Button(screen, text="portugues", command=portugues)
button2.pack()

button3 = tkinter.Button(screen, text="ingles", command=ingles)
button3.pack()
result1 = tkinter.Label(screen,text="resultado :")
result1.pack()
result = tkinter.Label(screen,text="")
result.pack()
warning = tkinter.Label(screen,text="aviso este software não funciona sem internet, e támbem é open source, ou seja pegue o código e faça o que quizer")
warning.pack()
screen.mainloop()
