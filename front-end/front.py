import tkinter as tk

root = tk.Tk() #Serve para criar uma janela
root.geometry("800x500")#Serve para determinar o tamanho da janela
root.title("Bolsa de Valores")#Serve para mudar o titulo da janela que vai abrir
label = tk.Label(root, text="Bolsa de Valores", font=("Arial", 20))#Serve como uma espece de espaco onde ficara as palavras
#label.pack(side="top")Indica a posicao do label na tela, nesse caso estou usando uma posicao pre determinada
label.pack(padx=25, pady=20)#Posicao determinada como se foce ponto cartesiano x e y
texbox = tk.Text(root, height=3 ,font=("Arial",15))#Sao as caixas de texto
texbox.pack(padx=10)
#myentry = tk.Entry(root)#Tambem sao caixas de texto mas apois apertar enter nao vai para proxima linha
#myentry.pack(padx=10)
#button = tk.Button(root, text='Clickn Me', font=('Arial', 15))#Criar um botao
#button.pack(padx=10)
buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text="1", font=("Arial",18))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)
btn2 = tk.Button(buttonframe, text="2", font=("Arial",18))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)
btn3 = tk.Button(buttonframe, text="3", font=("Arial",18))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)
btn4 = tk.Button(buttonframe, text="4", font=("Arial",18))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)
btn5 = tk.Button(buttonframe, text="5", font=("Arial",18))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)
btn6 = tk.Button(buttonframe, text="6", font=("Arial",18))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)
btn7 = tk.Button(buttonframe, text="7", font=("Arial",18))
btn7.grid(row=2, column=0, sticky=tk.W+tk.E)
btn8 = tk.Button(buttonframe, text="8", font=("Arial",18))
btn8.grid(row=2, column=1, sticky=tk.W+tk.E)
btn9 = tk.Button(buttonframe, text="9", font=("Arial",18))
btn9.grid(row=2, column=2, sticky=tk.W+tk.E)
btn10 = tk.Button(buttonframe, text="0", font=("Arial",18))
btn10.grid(row=3, column=0, sticky=tk.W+tk.E)
buttonframe.pack(fill='x')#O fill serve para completar, nesse caso vai completar tudo na eixo x

anotherbtn = tk.Button(root, text="Test", font=("Arial",18))
anotherbtn.place(x= 300, y=300, height=100, width=100)
root.mainloop()
