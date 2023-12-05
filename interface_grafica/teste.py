from tkinter import *
from tkinter import ttk

janela = Tk()
frm = ttk.Frame(janela, padding=10)
frm.grid()
ttk.Label(frm, text="Seja bem vindo! Nós da AttemporalBrand iremos te atender da melhor forma possível").grid(column=0, row=0)
ttk.Button(frm, text="Saiba mais", command=janela.destroy).grid(column=1, row=0)
janela.mainloop()