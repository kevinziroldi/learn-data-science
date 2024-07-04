import matplotlib.pyplot as plt
import csv
import numpy as np


# INTRODUZIONE, DIAGRAMMA CARTESIANO
x = [1,2,3]
y = [5,7,4]

x2 = [1,2,3]
y2 = [10,14,12]

plt.plot(x,y,label='First Line') # si genera già in background
plt.plot(x2,y2,label='Second Line')

plt.xlabel('Plot number') # nome asse x
plt.ylabel('Important var') # nome asse y
plt.title('Interesting Graph') # titolo del grafico
# volendo puoi fare un sottotitolo, ad es: plt.title('Interesting Graph\nSubtitle'), solo con \n, marcionata

plt.legend()

plt.show() # serve per mostarlo


# GRAFICO A BARRE

x = [2,4,6,8,10]
y = [6,7,8,2,4]

x2 = [1,3,5,7,9]
y2 = [7,8,2,4,2]
plt.bar(x,y,label=('Bars1'),color='#A6FBB2') # .bar serve per creare un grafico a barre
plt.bar(x2,y2,label=('Bars2'),color='c')
# i colori: posso metter alcuni prediniti, tipo 'blue' oppure le inziali 'r'=rosso, 'c'=ciano
# oppure posso mettere colori col #, ad esempio #A6FBB2 è verde menta chiaro
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()


# ISTOGRAMMA

population_ages = [22,55,62,45,6,98,23,45,76,38,103,67,43,56,48,12,130,111,80,45,23,48,76,95,14,27,35,48,98,65,63,38]
ids = [i for i in range(len(population_ages))]
plt.xlabel('x')
plt.ylabel('y')
plt.bar(ids,population_ages)
plt.show()
# non ha molto senso, sono robe messe tutte in ordine senza senso


# è meglio usare un'istogramma
population_ages = [22,55,62,45,6,98,23,45,76,38,103,67,43,56,48,12,130,111,80,45,23,48,76,95,14,27,35,48,98,65,63,38]
bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]

plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)
plt.xlabel('x')
plt.ylabel('y')
plt.show()


# SCATTER PLOT (grafico a puntini)

x = [1,2,3,4,5,6,7,8]
y = [3,5,6,2,5,8,6,4]

plt.scatter(x, y, label='skitscat', color='k', marker='*', s=1000)
# marker = cosa voglio che sia, anzichè il pallino
# s = size = dimensione del marker

plt.xlabel('x')
plt.ylabel('y')
plt.show()


# STACK PLOT 
# per mostrare la quantità di qualcosa nel totale

days = [1,2,3,4,5]
sleeping = [7,8,6,11,7]
eating = [2,3,4,3,2]
working = [7,8,7,2,2]
playing = [8,5,7,8,13]

plt.plot([],[],color='m',label='sleeping')
plt.plot([],[],color='c',label='eating')
plt.plot([],[],color='r',label='working')
plt.plot([],[],color='k',label='playing')
plt.stackplot(days, sleeping, eating, working, playing, colors=['m','c','r','k'])

plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.show()


# GRAFICO A TORTA (PIE CHART)

days = [1,2,3,4,5]
sleeping = [7,8,6,11,7]
eating = [2,3,4,3,2]
working = [7,8,7,2,2]
playing = [8,5,7,8,13]

slices = [7,2,2,13]
activities = ['sleeping','eating','working','playing']
cols = ['c','m','r','k']
 
plt.pie(slices,labels=activities,colors=cols,startangle=90,shadow=True, explode=(0,0.1,0,0),autopct=('%1.1f%%'))
plt.show()


# IMPORTARE DATI DA UN FILE

# possiamo farlo usando la libreria csv
x = []
y = []

with open ('tryMatplotlib.csv','r') as csvfile:
    plots = csv.reader(csvfile,delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))
        
plt.plot(x,y,label='Loaded from file')
        
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph')
plt.legend()
plt.show()


# oppure usando la libreria numpy

x, y = np.loadtxt('tryMatplotlib.csv',delimiter=',',unpack=True)

plt.plot(x,y,label='Loaded from file')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph')
plt.legend()
plt.show()
