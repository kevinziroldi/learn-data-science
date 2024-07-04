import numpy as np
from io import StringIO

# 1 - DICHIARAZIONE ARRAY
# per dichiarare un array: nomeVariabile = numpy.array (elementi del vettore)
# gli elementi si mettono tra parentesi quadre, separati da virgole, come un array normale

# array monodimensionale
a = np.array([1,2,3], dtype='int16')
print(a)

# array bidimensionale
b = np.array([[1,2,3],[4,5,6]])
print(b)


# 2 - funzione per avere la DIMENSIONE dell'ARRAY (monodimensionale, bidimensionale = vettore, matrice): ndim
# nomeArray.ndim

print('dimension a: ', a.ndim)
print('dimension b: ', b.ndim)


# 3 - funzione per avere la STRUTTURA, ritorna numero di righe e colonne: shape
# nomeArray.shape
# output: vettore con due parametri (numero righe, numero colonne)

print('shape a: ', a.shape)
print('shape b: ', b.shape)


# 4- funzione per ottenere il TIPO DI DATO, DIMENSIONE, MEMORIA OCCUPATA

# nomeArray.dtype, sta per data type
print(a.dtype)
print(b.dtype)
# se voglio posso impostare io la dimensione dell'array posso farlo in fase di dichiarazione
# ad esempio: a = np.array ([2,3,4], dtype = 'int 16')
# in generale devo mettere dtype = 'tipoDiDato' 

# funzione che ritorna il numero di byte: itemsize
# nomeArray.itemsize
print(a.itemsize)
print(b.itemsize)

# per ottenere il numero di elementi del vettore: funzione .size
# nomeArray.size
print(a.size)

# per ottenere la dimensione totale dell'array: nbytes
# ritorna la dimensione in byte dell'array,
# ogni elemento occupa 8/16/32/... bit ovvero 1/2/3 byte
# il totale sarà numero di elementi per dimensione dell'elemento in byte
print(a.nbytes)
# a.nbytes = a.size * a.itemsize


# 5 - modalità di ACCESSO e MODIFICA ad un vettore con numpy

c = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(c)
print(c.shape)
 
# per cercare un elemento in particolare
# nomeArray[riga,colonna]
# se voglio prendere il numero 12:
# si trova alla riga 1 (è la seconda e si inizia a contare da 0)
# si trova alla colonna 4 (quinta colonna, si inizia da 0)

print(c[1,4]) # output: 12

# potrei fare anche c[1,-3], (-1 è 14, scalo sempre di uno, come nelle liste)

# posso cercare una linea oppure una colonna, mette l'index della riga o della colonna e ":"
# per ottenere la prima riga:
print(c[0,:])

# per ottenere la quarta colonna:
print(c[:,3])

# posso fare anche cose più complicate, ad esempio se voglio 9,11,13
print(c[1,1:13:2])
# primo 1 = seconda riga, secondo 1 = secondo elemento della seconda riga, :13 elemento finale che cerco
# :2 di quanto devo saltare, 2 = uno sì e uno no

# accedendo ad un elemento posso visualizzare oppure cambiarlo
# ad esempio se volgio cambiare il 10 con 567:
c[1,2] = 567
print(c)
# allo stesso modo posso anche cambiare un'intera riga oppure un'intera colonna
c[0,:] = 3
print(c)

# prendiamo un array tridimensionale

d = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(d)
# se volgio il 5, procedo dall'esterno
# ci sono due insiemi grandi: il secondo, due sottoinsiemi: il primo, il primo di quel sottoinsieme
print(d[1,0,0])
# puoi sostituire anche in questo caso


# 6 - FUNZIONI PER INIZIALIZZARE

# ZEROS è una funzione che serve ad inizializzere a zero
# mi permette di dichiarare un array fatto da zeri
# può essere monodimensionale, bidimensionale, ... varie strutture
# sintassi: nomearray = numpy.zeros(struttura)
# es monodimensioanle
e = np.zeros(3)
print(e)
# es bidimensionale
f = np.zeros((3,4))
print(f)
# es cosa molto complessa
g = np.zeros((3,4,5))
print(g)

# ONES è uguale, ma inizializza a 1
h = np.ones((3,4))
print(h)

# posso anche inizializzare a numeri diversi da 0 e 1:
# funzione full
# x = np.full (struttura,numero a cui devo inizializzare)
i = np.full((2,3),88)
print(i)
# per passare la struttura posso mettere la struttura di un array già esistente
# passo nomeArrayEsistente.shape
l = np.full(a.shape,4)
print(l)
# stessa cosa di usare np.full_like
m = np.full_like(a,4)
print(m)
# l = m

# possiamo inizializzare a numeri decimali random
n = np.random.rand(4,2) # ! attenzione perchè le parentesi sono diverse
print(n)
# per usare la forma di un altro array si usa random.random_sample
o = np.random.random_sample(a.shape)
print(o)

# mentre se voglio random interi uso randint
p = np.random.randint(2,7, size=(3,3))
print(p)
# per generare un numero casuale solo np.random.randint(nmin,nmax)

# identity matrix, per come è fatta è un quadrato
q = np.identity(3)
print(q)


# per ripetere: np.repeat
r = np.repeat(a,4)
print(r)

output = np.ones((5,5))
print(output)
centro = np.zeros((3,3))
centro[1,1] = 9
output[1:4,1:4] = centro
print(output)



# ATTENZIONE QUANDO COPI ARRAY
# se io faccio ho un array a e scrivo a = b diventano la stessa cosa
# se modifico uno, modifico anche l'altro
# devo usare .copy()
a = [1,2,3]
b = a
b[0] = 100
print(a)
# avrò [100,2,3]
#invece uso .copy()
a = [1,2,3]
b = a.copy()
b[0] = 100
print(a)


# MATEMATICA
# posso fare:
# + 
# -
# *
# /
# ** = esponente
# tutte le operazioni sono fatte su tutti gli elementi dell'array

a = [1,2,3] # crea nuovi elementi, allunga il vettore in pratica
a *= 2
print(a)

b = np.array([1,2,3]) # moltiplica per due gli elementi
b *= 2
print(b)

b += 3 # posso fare la somma, cosa che con gli array normali non si può fare
print(b) 

c = np.array([[2,3,4],[3,6,7],[4,6,7]])
c = c/2
print(c)

# posso sommre array tra loro, sommo primo elemento con primo elemento e così via

a = np.array([1,2,3])
b = np.array([5,8,2])
print(a+b)

# permette di farlo solo se hanno lo stesso numero di elementi

# ha anche sin, cos
# gli angoli sono in radianti
a = np.array([1.57])
print(np.sin(a))



# ALGEBRA LINEARE

a = np.ones((2,3))
print(a)
b = np.full((3,2),2)
print(b)

prodotto = np.matmul(a,b)
print(prodotto)

# posso trovare il determinante di una matrice quadrata

a = np.identity(3)
print(np.linalg.det(c))


# STATISSTICA
# ha funzioni come min, max
# posso farlo sia di tutta la matrice che di una singola riga o colonna

a = np.array([[1,2,3],[4,5,6]])
print(a)
print(np.max(a))
print(np.min(a))

# sum mi da la somma degli elementi 
print(np.sum(a))


# RIORGANIZZAZIONE ARRAYS
# si usa la funzione reshape

before = np.array([[1,2,3,4],[5,6,7,8]])
print(before)
print(before.shape)

after = before.reshape((2,2,2))
print(after)

# per organizzare impilare array, uso vstack (vertical)
a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.vstack([a,b]))
# posso anche ripeterli
print(np.vstack([a,b,a,b,b]))

# posso impilare anche in orizzontale, uso hstack (horizontal)
a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.hstack([b,a]))


# posso importare dati da file di testo
# si usa la funzione
# np.genfromtxt('nomeFile', delimiter='ciò che separa i dati, ad esempio la virgola')

filedata = np.genfromtxt('data.txt',delimiter=',')
print(filedata)
# data.txt è il nome del file

# per cambiare il tipo
filedata = filedata.astype('int32')
print(filedata)



# se voglio vedere delle proprietà del mio array: 
print(filedata > 2) # me li stamoa con la stessa forma dell'array

# mentre per avere i valori:
print(filedata[filedata>2])

# index a list with numpy
a = np.array([1,2,3,4,5,6,7,8,9])
print(a[[0,2,8]])
# posso combinare condizioni
print((filedata>3) & (filedata<8))

# a[[0,4,5],3:]