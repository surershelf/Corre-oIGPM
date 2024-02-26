import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox


IGPM = {
    "2004": {
        "jan": 0.88,
        "fev": 0.69,
        "mar": 1.13,
        "abr": 1.21,
        "mai": 1.31,
        "jun": 1.38,
        "jul": 1.31,
        "ago": 1.22,
        "set": 0.69,
        "out": 0.39,
        "nov": 0.82,
        "dez": 0.74
    },
    "2005": {
        "jan": 0.39,
        "fev": 0.30,
        "mar": 0.85,
        "abr": 0.86,
        "mai": -0.22,
        "jun": -0.44,
        "jul": -0.34,
        "ago": -0.65,
        "set": -0.53,
        "out": 0.60,
        "nov": 0.40,
        "dez": -0.01
    },
    "2006": {
        "jan": 0.92,
        "fev": 0.01,
        "mar": -0.23,
        "abr": -0.42,
        "mai": 0.38,
        "jun": 0.75,
        "jul": 0.18,
        "ago": 0.37,
        "set": 0.29,
        "out": 0.47,
        "nov": 0.75,
        "dez": 0.32
    },
    "2007": {
        "jan": 0.50,
        "fev": 0.27,
        "mar": 0.34,
        "abr": 0.04,
        "mai": 0.04,
        "jun": 0.26,
        "jul": 0.28,
        "ago": 0.98,
        "set": 1.29,
        "out": 1.05,
        "nov": 0.69,
        "dez": 1.76
    },
    "2008": {
        "jan": 1.09,
        "fev": 0.53,
        "mar": 0.74,
        "abr": 0.69,
        "mai": 1.61,
        "jun": 1.98,
        "jul": 1.76,
        "ago": -0.32,
        "set": 0.11,
        "out": 0.98,
        "nov": 0.38,
        "dez": -0.13
    },
    "2009": {
        "jan": -0.44,
        "fev": 0.26,
        "mar": -0.74,
        "abr": -0.15,
        "mai": -0.07,
        "jun": -0.10,
        "jul": -0.43,
        "ago": -0.36,
        "set": 0.42,
        "out": 0.05,
        "nov": 0.10,
        "dez": -0.26
    },
    "2010": {
        "jan": 0.63,
        "fev": 1.18,
        "mar": 0.94,
        "abr": 0.77,
        "mai": 1.19,
        "jun": 0.85,
        "jul": 0.15,
        "ago": 0.77,
        "set": 1.15,
        "out": 1.01,
        "nov": 1.45,
        "dez": 0.69
    },
    "2011": {
        "jan": 0.79,
        "fev": 1.00,
        "mar": 0.62,
        "abr": 0.45,
        "mai": 0.43,
        "jun": -0.18,
        "jul": -0.12,
        "ago": 0.44,
        "set": 0.65,
        "out": 0.53,
        "nov": 0.50,
        "dez": -0.12
    },
    "2012": {
        "jan": 0.25,
        "fev": -0.06,
        "mar": 0.43,
        "abr": 0.85,
        "mai": 1.02,
        "jun": 0.66,
        "jul": 1.34,
        "ago": 1.43,
        "set": 0.97,
        "out": 0.02,
        "nov": -0.03,
        "dez": 0.68
    },
    "2013": {
        "jan": 0.34,
        "fev": 0.29,
        "mar": 0.21,
        "abr": 0.15,
        "mai": 0.00,
        "jun": 0.75,
        "jul": 0.26,
        "ago": 0.15,
        "set": 1.50,
        "out": 0.86,
        "nov": 0.29,
        "dez": 0.60
    },
    "2014": {
        "jan": 0.48,
        "fev": 0.38,
        "mar": 1.67,
        "abr": 0.78,
        "mai": -0.13,
        "jun": -0.74,
        "jul": -0.61,
        "ago": -0.27,
        "set": 0.20,
        "out": 0.28,
        "nov": 0.98,
        "dez": 0.62
    },
    "2015": {
        "jan": 0.76,
        "fev": 0.27,
        "mar": 0.98,
        "abr": 1.17,
        "mai": 0.41,
        "jun": 0.67,
        "jul": 0.69,
        "ago": 0.28,
        "set": 0.95,
        "out": 1.89,
        "nov": 1.52,
        "dez": 0.49
    },
    "2016": {
        "jan": 1.14,
        "fev": 1.29,
        "mar": 0.51,
        "abr": 0.33,
        "mai": 0.82,
        "jun": 1.69,
        "jul": 0.18,
        "ago": 0.15,
        "set": 0.20,
        "out": 0.16,
        "nov": -0.03,
        "dez": 0.54
      },
    "2017": {
        "jan": 0.64,
        "fev": 0.08,
        "mar": 0.01,
        "abr": -1.10,
        "mai": -0.93,
        "jun": -0.67,
        "jul": -0.72,
        "ago": 0.10,
        "set": 0.47,
        "out": 0.20,
        "nov": 0.52,
        "dez": 0.89
    },
    '2018': {
        'jan': 0.76,
        'fev': 0.07,
        'mar': 0.64,
        "abr": 0.57,
        "mai": 1.38,
        "jun": 1.87,
        "jul": 0.51,
        "ago": 0.70,
        "set": 1.52,
        "out": 0.89,
        "nov": -0.49,
        "dez": -1.08,
    },
    "2019": {
        "jan": 0.01,
        "fev": 0.88,
        "mar": 1.26,
        "abr": 0.92,
        "mai": 0.45,
        "jun": 0.80,
        "jul": 0.40,
        "ago": -0.67,
        "set": -0.01,
        "out": 0.68,
        "nov": 0.30,
        "dez": 2.09
    },
        "2020": {
            "jan": 0.48,
            "fev": -0.04,
            "mar": 1.24,
            "abr": 0.80,
            "mai": 0.28,
            "jun": 1.56,
            "jul": 2.23,
            "ago": 2.74,
            "set": 4.34,
            "out": 3.23,
            "nov": 3.28,
            "dez": 0.96
        },
        "2021": {
            "jan": 2.58,
            "fev": 2.53,
            "mar": 2.94,
            "abr": 1.51,
            "mai": 4.10,
            "jun": 0.60,
            "jul": 0.78,
            "ago": 0.66,
            "set": -0.64,
            "out": 0.64,
            "nov": 0.02,
            "dez": 0.87
        },
        "2022": {
            "jan": 1.82,
            "fev": 1.83,
            "mar": 1.74,
            "abr": 1.41,
            "mai": 0.52,
            "jun": 0.59,
            "jul": 0.21,
            "ago": -0.70,
            "set": -0.95,
            "out": -0.97,
            "nov": -0.56,
            "dez": 0.45
        },
        "2023": {
            "jan": 0.21,
            "fev": -0.06,
            "mar": 0.05,
            "abr": -0.95,
            "mai": -1.84,
            "jun": -1.93,
            "jul": -0.72,
            "ago": -0.14,
            "set": 0.37,
            "out": 0.50,
            "nov": 0.59,
            "dez": 0.74,
        },
        "2024": {

        }
    }

meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']

def Igpm():

    igpm_total=0

    juros=float(input('Juros: '))
    lote_a_corrigir=float(input('Valor do lote a ser corrigido:'))
    a=int(input('De quando começaremos a calcular o IGPM: '))
    b=int(input('Até quando?'))



    for ano in range(a,b + 1):
        for mes, valor in IGPM[str(ano)].items():
            if valor >= 0 :
                igpm_total += valor

    igpm_jur =igpm_total+ juros
    juros_pc= igpm_jur / 100
    v_j=lote_a_corrigir*juros_pc
    valor_tot=lote_a_corrigir + v_j

    print(f"IGPM total de {a} a {b}: {igpm_total:.2f}")
    print(f"O valor de juros + IGPM é de: {igpm_jur:.2f}%")
    print(f'O valor adicional é de R${v_j}')
    print(f'O valor corrigido do lote é de: {valor_tot:.2f}')


def somar_valores():
    global igpm_jur, v_j, resultado
    igpm_total = 0

    juros = caixa_texto1.get()
    lote_a_corrigir = caixa_texto2.get()
    a = caixa_texto3.get()
    b = caixa_texto4.get()

    #tratamento de erros

    try:
        juros = float(juros.replace(',', '.'))
        lote_a_corrigir = float(lote_a_corrigir.replace(',', '.'))
        a = int(a)
        b = int(b)
    except ValueError:
        messagebox.showerror('Erro: Insira valores numéricos válidos.', parent=janela)
        return


    mes_inicial = meses.index(caixa_mes_inicial.get())
    mes_final = meses.index(caixa_mes_final.get())

    if a == b and mes_inicial > mes_final:
        messagebox.showerror("Erro: O mês inicial não pode ser maior que o mês final para o mesmo ano.",parent=janela)
        return

    for ano in range(a, b + 1):
        for mes, valor in IGPM[str(ano)].items():
            if (ano == a and meses.index(mes) >= mes_inicial) or (ano == b and meses.index(mes) <= mes_final) or (a < ano < b):
                if valor >= 0:
                    igpm_total += valor

    igpm_jur = igpm_total + juros
    mensagem_igpm.config(text=f"Porcentagem Adicional: {igpm_jur:.2f}%")

    juros_pc = igpm_jur / 100

    v_j = lote_a_corrigir * juros_pc
    mensagem_v_j.config(text=f"Valor Adicional: R$ {v_j:.2f}")

    resultado = lote_a_corrigir + v_j
    mensagem_resultado.config(text=f"Resultado: R$ {resultado:.2f}")


janela = tk.Tk()
janela.geometry("1080x720")
janela.title("Correção de Imóvel")

janela.configure(bg="#87CEEB")
fonte_menor=("Arial",13)
fonte_maior=("Arial",16)


juros = tk.Label(janela, text="Juros Total:",font=fonte_menor,bg="#87CEEB")
juros.place(x=20,y=90)
caixa_texto1 = tk.Entry(janela)
caixa_texto1.place(x=20,y=110)


valor_lote = tk.Label(janela, text="Valor Lote:",font=fonte_menor,bg="#87CEEB")
valor_lote.place(x=20,y=180)
caixa_texto2 = tk.Entry(janela)
caixa_texto2.place(x=20,y=200)

ano_inicial = tk.Label(janela, text="Do ano:",font=fonte_menor,bg="#87CEEB")
ano_inicial.place(x=20,y=260)
caixa_texto3 = tk.Entry(janela)
caixa_texto3.place(x=20,y=280)

Mes_Inicial = tk.Label(janela, text="Mês Inícial:", font=fonte_menor,bg="#87CEEB")
Mes_Inicial.place(x=20, y=330)
caixa_mes_inicial = ttk.Combobox(janela, values=meses)
caixa_mes_inicial.place(x=20, y=350)

ate = tk.Label(janela, text="Até:",font=fonte_menor,bg="#87CEEB")
ate.place(x=20,y=410)
caixa_texto4 = tk.Entry(janela)
caixa_texto4.place(x=20,y=430)

Final = tk.Label(janela, text="Mês Final:", font=fonte_menor,bg="#87CEEB")
Final.place(x=20, y=490)
caixa_mes_final = ttk.Combobox(janela, values=meses)
caixa_mes_final.place(x=20, y=510)


botao_somar = tk.Button(janela, text="Somar", command=somar_valores,font=fonte_maior,bg="#87CEEB")
botao_somar.place(x=450,y=320)

igpm_jur=0
mensagem_igpm = tk.Label(janela, text="Porcentagem Total: {:.2f}%".format(igpm_jur),font=fonte_maior,bg="#87CEEB")
mensagem_igpm.place(x=750,y=150)

v_j=0
mensagem_v_j= tk.Label(janela,text="Valor adicional:R$ {:.2f}".format(v_j), font=fonte_maior,bg="#87CEEB")
mensagem_v_j.place(x=750,y=300)

resultado=0
mensagem_resultado = tk.Label(janela, text="Valor Corrigido:R$ {:.2f}".format(resultado),font=fonte_maior,bg="#87CEEB")
mensagem_resultado.place(x=750,y=450)

janela.mainloop()
