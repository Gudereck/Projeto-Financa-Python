from tkinter import *
from tkinter import Tk, ttk 
from PIL import Image, ImageTk
#Barra de progresso
from tkinter.ttk import Progressbar

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
################# cores ###############
co0 = "#2e2d2b"  
co1 = "#feffff"  
co2 = "#4fa882"  
co3 = "#38576b"  
co4 = "#403d3d"  
co5 = "#e06636"  
co6 = "#038cfc"  
co7 = "#3fbfb9"  
co8 = "#263238"  
co9 = "#e9edf5"  

colors = ['#5588bb', '#66bbbb','#99bb55', '#ee9944', '#444466', '#bb5555']

#criando janela
janela = Tk()
janela.title("Calculadora de Finanças")
janela.geometry('900x650')
janela.configure(bg=co9)
janela.resizable(width = False, height=False)

style = ttk.Style(janela)
style.theme_use("clam")

#criando frames
frame_cima = Frame(janela, width=1043, height=50, bg=co1, relief="flat")
frame_cima.grid(row=0, column =0)

frame_meio = Frame(janela, width=1043, height=361, bg=co1,pady=20, relief="raised")
frame_meio.grid(row=1, column =0, pady=1, padx=0, sticky=NSEW)


frame_baixo = Frame(janela, width=1043, height=300, bg=co1, relief="flat")
frame_baixo.grid(row=2, column =0, pady= 0, padx=10, sticky=NSEW)

##trabalhando no frame cima

#Acessando a imagem

app_img = Image.open('Logo.png') 
app_img = app_img.resize((45, 45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frame_cima, image = app_img,width=900,text = " Finanças", compound=LEFT, padx=5,  anchor=NW, font=('Verdana 20 bold'), bg=co1, fg=co4)
app_logo.place(x=0, y=0) # Lembre-se de posicionar o logo

##Porcentagem

# Pequena alteração necessária para a função aceitar um valor
def porcentagem(valor_atual):
    l_nome = Label(frame_meio, text = "Porcentagem da Receita gasta",height=1, anchor=NW, font=('Verdana 12'),bg=co1,fg=co4)
    l_nome.place(x=7, y=5)
    
    # --- INÍCIO DA ADIÇÃO ---
    # Mantendo a criação do estilo aqui dentro, como no seu código original
    style=ttk.Style()
    style.theme_use('default')
    
    # Cores que vamos usar para os estilos
    laranja = '#ee9944'
    vermelho = '#bb5555'

    # Adicionamos a configuração para as 3 cores
    style.configure("Green.Horizontal.TProgressbar", thickness=20, troughcolor=co1, background=co2)
    style.configure("Orange.Horizontal.TProgressbar", thickness=20, troughcolor=co1, background=laranja)
    style.configure("Red.Horizontal.TProgressbar", thickness=20, troughcolor=co1, background=vermelho)
    # --- FIM DA ADIÇÃO ---
    
    # Alteração mínima para usar um dos novos estilos na criação da barra
    bar = Progressbar(frame_meio, length=180, style="Green.Horizontal.TProgressbar",)
    bar.place(x=10, y=35)
    bar['value'] = valor_atual# Usamos o valor que a função recebeu
     # Você pode mudar esse valor para testar as cores

    # --- ADIÇÃO DA LÓGICA IF/ELSE ---
    # Este bloco decide qual cor (estilo) usar com base no valor
    if valor_atual < 20:
        bar.config(style="Red.Horizontal.TProgressbar")
    elif valor_atual < 50:
        bar.config(style="Orange.Horizontal.TProgressbar")
    else: # Se for 50 ou mais
        bar.config(style="Green.Horizontal.TProgressbar") 

    l_Porcentagem = Label(frame_meio, text = "{:,.2f}%".format(valor_atual),height=1, anchor=NW, font=('Verdana 12'),bg=co1,fg=co4)
    l_Porcentagem.place(x=200, y=35)

#função para grafico bar
def grafico_bar():
    lista_categorias = ['Renda', 'Despesas', 'Saldo']
    lista_valores = [3000,2000,1000]
    figura = plt.Figure(figsize=(4, 3.45), dpi=60)
    ax = figura.add_subplot(111)
    ax.bar(lista_categorias, lista_valores,  color=colors, width=0.9)
    c = 0
    #set individual bar lables using above list
    for i in ax.patches:
     #get_x pulls left or right; get_height pushes up or down
     ax.text(i.get_x()-.001, i.get_height()+.5,
                str("{:,.0f}".format(lista_valores[c])), fontsize=17, fontstyle='italic',  verticalalignment='bottom',color='dimgrey')
     c += 1

    ax.set_xticklabels(lista_categorias,fontsize=16)

    ax.patch.set_facecolor('#ffffff')
    ax.spines['bottom'].set_color('#CCCCCC')
    ax.spines['bottom'].set_linewidth(1)
    ax.spines['right'].set_linewidth(0)
    ax.spines['top'].set_linewidth(0)
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['left'].set_linewidth(1)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(bottom=False, left=False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(False, color='#EEEEEE')
    ax.xaxis.grid(False)

    canva = FigureCanvasTkAgg(figura, frame_meio)
    canva.get_tk_widget().place(x=10, y=70) 

grafico_bar()
porcentagem(65) # Chame a função com o valor desejado
janela.mainloop()