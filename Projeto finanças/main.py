from tkinter import *
from tkinter import Tk, ttk 
from PIL import Image, ImageTk
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




janela.mainloop()