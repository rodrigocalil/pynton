#!/usr/bin/env python
# -*- coding: utf-8 -*-



import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from math import *

class Application:

    def iniciaConexao(self):
        try:
            self.con = sqlite3.connect('database.db')
            cursor = self.con.cursor()
            cursor.execute("drop table if exists imc;")

            cursor.execute("CREATE TABLE imc (nome TEXT,imc TEXT NOT NULL);")
            print(cursor.fetchall())

            cursor.execute("select sql from sqlite_master where type = 'table' and name = 'imc';")
            print(cursor.fetchall())
            sqlite_select_Query = "select sqlite_version();"
            cursor.execute(sqlite_select_Query)
            record = cursor.fetchall()
            print("Conectado com a base de dados com sucesso. Versao: ",record)
            cursor.close()


        except sqlite3.Error as error:
            print("Erro ao conectar com o banco de dados. Permissão de escrita?", error)
        return self.con


    def __init__(self, master=None):
        con = self.iniciaConexao()
        self.fonte1 = ("Arial"), ("10")

        self.espaco0 = Frame(master)
        self.espaco0["pady"] =30
        self.espaco0.pack()

        self.espaco1 = Frame(master)
        self.espaco1.pack()

        self.espaco2 = Frame(master)
        self.espaco2.pack()

        self.espaco3 = Frame(master)
        self.espaco3["pady"] = 40
        self.espaco3.pack()

        self.espaco4 = Frame(master)
        self.espaco4.pack()

        self.espaco5 = Frame(master)
        self.espaco5.pack()

        self.espaco6 = Frame(master)
        self.espaco6.pack()

        self.nomeLabel = Label(self.espaco0, text="Nome do Paciente", font=self.fonte1)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.espaco0)
        self.nome["width"] = 30
        self.nome["font"] = self.fonte1
        self.nome.pack(side = LEFT)

        self.endLabel = Label(self.espaco1, text="Endereço completo", font=self.fonte1)
        self.endLabel.pack(side = LEFT)

        self.endInput = Entry(self.espaco1)
        self.endInput["width"] = 30
        self.endInput["font"] = self.fonte1
        self.endInput.pack(side = LEFT)

        self.alturaLabel = Label(self.espaco3, text="Altura (cm)", font=self.fonte1)
        self.alturaLabel.pack(side=LEFT)

        self.alturainput = Entry(self.espaco3)
        self.alturainput["width"] = 10
        self.alturainput["font"] = self.fonte1
        self.alturainput.pack(side=LEFT)

        self.pesoLabel = Label(self.espaco3, text="Peso (Kg)", font=self.fonte1)
        self.pesoLabel.place(y=30)

        self.pesoInput = Entry(self.espaco3)
        self.pesoInput["width"] = 10
        self.pesoInput["font"] = self.fonte1
        self.pesoInput.place(x=70,y=35)



        
        self.calcular = Button(self.espaco6)
        self.calcular["text"] = "CALCULAR"
        self.calcular["font"] = ("Calibri", "8")
        self.calcular["width"] = 12
        self.calcular["command"] = self.calcula
        self.calcular.pack(side = LEFT)

        self.consultar = Button(self.espaco6)
        self.consultar["text"] = "Consultar"
        self.consultar["font"] = ("Calibri", "8")
        self.consultar["width"] = 12
        self.consultar["command"] = self.consultarNome
        self.consultar.pack(side=LEFT)

        
        self.reiniciar = Button(self.espaco6)
        self.reiniciar["text"] = "Reiniciar"
        self.reiniciar["font"] = ("Calibri", "8")
        self.reiniciar["width"] = 12
        self.reiniciar["command"] = self.reinicia
        self.reiniciar.pack(side=LEFT)

        
        self.sair = Button(self.espaco6)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "8")
        self.sair["width"] = 12

        self.sair["command"] = root.destroy
        self.sair.pack(padx=50,side=RIGHT)


        self.text = Text(self.espaco3, height=10, width=20)

        self.text.tag_bind('bite',
                      '<1>',
                      lambda e, t=self.text: t.insert(END, ""))
        self.text.pack(padx=5, pady=20, side = RIGHT)

    def consultarNome(self):
        cursor = self.con.cursor()
        if self.nome.get():
            query = "select * from imc where nome = '"+self.nome.get()+"';"
            print(query)
            cursor.execute(query)
            record = cursor.fetchall()
            print(record)
            if (record):
                self.text.insert(END,record,2)
            else:
                "Não há consultas registradas para este nome"


    def gravarNome(self):
        cursor = self.con.cursor()
        if self.nome.get():
            query = "insert into imc(nome,imc) values ('"+self.nome.get()+"','"+str(self.imc)+"');"
            print(query)
            cursor.execute(query)
            record = cursor.fetchall()
            print(record)
            self.text.insert(END,"",2) if (len(record) > 0) else "Não há consultas registradas para este nome"
            self.text.pack() if (len(record) > 0) else ""


    def calcula(self):
        altura = (self.alturainput.get())
        peso = float(self.pesoInput.get())

        resp = (float(peso) / (float(altura)*float(altura)))

        if peso:
            self.text.insert(END,round(resp*10000,2))
            self.imc = round(resp*10000,2)
            self.text.pack()

        MsgBox = tk.messagebox.askquestion('Gravar', 'Deseja gravar o calculo do IMC?',
                                           icon='info')
        if MsgBox == 'yes':
            self.gravarNome()
        else:

            tk.messagebox.showinfo('Return', 'Gravação cancelada.')

    def reinicia(self):
       self.text.delete('1.0', END)
       

root = Tk()
root.title("Cálculo do IMC - índice de Massa Corporal")
root.geometry("400x450")
app = Application(root)
root.mainloop()
