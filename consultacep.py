import requests
import json
from tkinter import *

def consultaCep():
    try:
        cep = cepdigitado.get()
        req = requests.get('https://cep.awesomeapi.com.br/json/' + cep)
        formatado = json.loads(req.text)
        textorua["text"] = formatado['address']
        textocity["text"] = formatado['city']
    except:
        textorua["text"] = 'erro'


janela = Tk()
janela.title("Consulta por CEP")
janela.geometry("330x100")
janela.configure(background="#dde")

cepdigit = Label(janela, text="Informe o CEP:", background="#dde", foreground="#009", anchor=W)
cepdigit.grid(column=0, row=0)
cepdigitado = Entry(janela)
cepdigitado.grid(column=1, row=0)

botao = Button(janela, text="Clique", command=consultaCep)
botao.grid(column=2, row=0)

texto = Label(janela, text="Rua:", background="#dde", foreground="#009")
texto.grid(column=0, row=1)
textorua = Label(janela, text="", background="#dde", foreground="#009")
textorua.grid(column=1, row=1)

textocid = Label(janela, text="cidade:", background="#dde", foreground="#009")
textocid.grid(column=0, row=2)
textocity = Label(janela, text="", background="#dde", foreground="#009")
textocity.grid(column=1, row=2)

janela.mainloop()
