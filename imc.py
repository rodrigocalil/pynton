from tkinter import *
from math import *

class Application:
    def __init__(self, master=None):
        self.fonte1 = ("Arial"), ("10")

        self.espaço0 = Frame(master)
        self.espaço0["pady"] =30
        self.espaço0.pack()

        self.espaço1 = Frame(master)
        self.espaço1.pack()

        self.espaço2 = Frame(master)
        self.espaço2.pack()

        self.espaço3 = Frame(master)
        self.espaço3["pady"] = 40
        self.espaço3.pack()

        self.espaço4 = Frame(master)
        self.espaço4.pack()

        self.espaço5 = Frame(master)
        self.espaço5.pack()

        self.espaço6 = Frame(master)
        self.espaço6.pack()

        self.nomeLabel = Label(self.espaço0, text="Nome do Paciente", font=self.fonte1)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.espaço0)
        self.nome["width"] = 30
        self.nome["font"] = self.fonte1
        self.nome.pack(side = LEFT)

        self.endLabel = Label(self.espaço1, text="Endereço completo", font=self.fonte1)
        self.endLabel.pack(side = LEFT)

        self.endInput = Entry(self.espaço1)
        self.endInput["width"] = 30
        self.endInput["font"] = self.fonte1
        self.endInput.pack(side = LEFT)

        self.alturaLabel = Label(self.espaço3, text="Altura (cm)", font=self.fonte1)
        self.alturaLabel.pack(side=LEFT)

        self.alturainput = Entry(self.espaço3)
        self.alturainput["width"] = 10
        self.alturainput["font"] = self.fonte1
        self.alturainput.pack(side=LEFT)

        self.pesoLabel = Label(self.espaço3, text="Peso (Kg)", font=self.fonte1)
        self.pesoLabel.place(y=30)

        self.pesoInput = Entry(self.espaço3)
        self.pesoInput["width"] = 10
        self.pesoInput["font"] = self.fonte1
        self.pesoInput.place(x=70,y=35)



        
        self.calcular = Button(self.espaço6)
        self.calcular["text"] = "CALCULAR"
        self.calcular["font"] = ("Calibri", "8")
        self.calcular["width"] = 12
        self.calcular["command"] = self.calcula
        self.calcular.pack(side = LEFT)

        
        self.reiniciar = Button(self.espaço6)
        self.reiniciar["text"] = "Reiniciar"
        self.reiniciar["font"] = ("Calibri", "8")
        self.reiniciar["width"] = 12
        self.reiniciar["command"] = self.reinicia
        self.reiniciar.pack(side=LEFT)

        
        self.sair = Button(self.espaço6)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "8")
        self.sair["width"] = 12

        self.sair["command"] = root.destroy
        self.sair.pack(padx=50,side=RIGHT)


        self.text = Text(self.espaço3, height=10, width=20)

        self.text.tag_bind('bite',
                      '<1>',
                      lambda e, t=self.text: t.insert(END, ""))
        self.text.pack(padx=5, pady=20, side = RIGHT)

    
    def calcula(self):
        altura = (self.alturainput.get())
        peso = float(self.pesoInput.get())

        resp = (float(peso) / (float(altura)*float(altura)))

        if peso:
            self.text.insert(END,round(resp*10000,2))
            self.text.pack()


    def reinicia(self):
       self.text.delete('1.0', END)
       

root = Tk()
root.title("Cálculo do IMC - índice de Massa Corporal")
root.geometry("400x450")
Application(root)

root.mainloop()
