import pandas as pd

ds = pd.DataFrame({'Età':['16','18'],'Peso':['60','70']}, index=['persona1','persona2'])
print(ds)

series = pd.Series(['a','b','c'])
print(series)
# una serie è una colonna di un dataframe

# la maggior parte delle volte i dati che utilizzi li prendi
# spoesso si usano file CSV (comma-separated values)
# per leggerli esiste una funzione
# pd.read_csv()
# per vedere il percorso del file basta trascinarlo nel terminale

# per sapere come è fatto .shape
# mentre per visualizzare le prime cinque righe uso .head()

# nella funzione .read_csv() si possono specificare molte cose
# ad esempio posso specificare che la prima colonna è l'indice se nel file CSV è così

fruits = pd.DataFrame({'Apples':[30],'Bananas':[21]})
print(fruits)

fruit_sales = pd.DataFrame({'Apples':[35,41],'Bananas':[21,34]},index=['2017 Sales','2018 Sales'])
print(fruit_sales)

ingredients = pd.Series(['4 cups','1 cup','2 large','1 can'],index=['Flour','Milk','Eggs','Spam'], name='Dinner',dtype='object')
print(ingredients)


# reviews = pd.read_csv('../input/wine-reviews/winemag-data_first150k.csv',index_col=0)
# non ho il file

animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])
print(animals)


# animals.to_csv('cows_and_goats.csv')
# ogni volta mi crea il file


reviews = pd.DataFrame({'country':['italy','potugual','france','italy'],'description':['good','so so','bad','very good'],'points':[90,54,67,98]})
print(reviews)

# per stampare 'points'
print('points:')
print(reviews.points)
# oppure
print(reviews['points'])

# per stampare 'portugual'
print(reviews.country[1])
# per stampare 'so so'
print(reviews['description'][1])


# loc, iloc sono entrambi (row,colums) al contrario di python dove è (column,row)

# iloc = Index-based selection
# iloc si basa sulla posizione numerica degli elementi, righe o colonne
# volgio stampare colonna points primo e secondo
print(reviews)
print(reviews.iloc[0:2,2])
# per stampare tutto della prima riga (italia)
print(reviews.iloc[0,:])
# posso anche passare liste
print(reviews.iloc[[0,1],0])

# loc = Label-based selection
# si basa sul label, ovvero l'etichetta
# usa l'etichetta della colonna e l'indice della riga
# per stampare 'good'
print(reviews.loc[0,'description'])

# ATTENZIONE i due punti ":" sono diversi in iloc e loc
# i ":" di iloc sono esclusivi, come in python: primi 4 elementi .iloc[0:4] (0,1,2,3) oppure .iloc[:4]
# i ":" di loc sono inclusivi: i primi 4 .loc[0:3] (0,1,2,3) oppure .loc[:3]
# perchè loc lo uso anche con char o stringhe, ... diventa scomodo prendere la lettera successiva, la parola perde di significato


# l'index può essere modificato
# .set_index("nomeEtichetta")
# per esempio metto come indice di reviews la nazione
'''
print(reviews)
reviews = reviews.set_index('country')
print(reviews)
'''
# lascio come commento altrimenti mi sminchia tutto la roba dopo


# per selezionare degli elementi con una determinata caratteristica
print(reviews.country == 'italy') # stampa true e false
# mentre per selezionarli
# reviews.loc[reviews.country == 'italy']
print(reviews.loc[reviews.country == 'italy'])
# posso usare & e | per combinare condizioni
# & = e, devono essere entrambe vere
# reviews.loc[(reviews.country == 'italy') & (reviews.points > 80)]
# | = o, almeno una, o una, o l'altra o entrambe


# .isin e .isnull sono delle funzioni di pandas per selezionare
reviews.loc[reviews.country.isin(['italy', 'france'])] # dati che hanno il valore che indico
# is null, ha un elemento vuoto
reviews.loc[reviews.description.isnull()]
# not null, non ha elementi vuoti
reviews.loc[reviews.description.notnull()]


# posso aggiungere un parametro
# costante:
reviews['critic'] = 'everyone'
print(reviews)
# iterable
reviews['a'] = range(len(reviews), 0, -1)
print(reviews)


# Select the description column from reviews and assign the result to    the variable desc
desc = reviews.description

# Select the first value from the description column of reviews, assigning it to variable first_description
first_description = reviews.description.iloc[0]

# Select the first row of data (the first record) from reviews, assigning it to the variable first_row
first_row = reviews.iloc[0]

# Select the first 10 values from the description column in reviews, assigning the result to variable first_descriptions
first_descriptions = reviews.loc[0:9,'description']

# Select the records with index labels 1, 2, 3, 5, and 8, assigning the result to the variable sample_reviews.
# sample_reviews = reviews.iloc[[1,2,3,5,8]]

# Create a variable df containing the country, province, region_1, and region_2 columns of the records with the index labels 0, 1, 10, and 100
# df = reviews.loc[[0,1,10,100],['country','province','region_1','region_2']]

# Create a variable df containing the country and variety columns of the first 100 records
# df = reviews.loc[0:99,['country','variety']]

# Create a DataFrame italian_wines containing reviews of wines made in Italy
italian_wines = reviews.loc[reviews.country == 'Italy']

# Create a DataFrame top_oceania_wines containing all reviews with at least 95 points (out of 100) for wines from Australia or New Zealand
top_oceania_wines = reviews.loc[(reviews.country.isin(['Australia','New Zealand'])) & (reviews.points >= 95)]



# funzioni python 'riassuntive' ovvero che danno dei valori medi/generali sui dati

# funzione .describe() che è type-aware, ovvero l'output dipende dal tipo di dato

print(reviews)
print(reviews.points.describe())
print(reviews.country.describe())

# possiamo usare .mean() per fare la media dei valori di una serie oppure di una colonna di un dataframe
print(reviews.points.mean())

# per ottenere la lista di valori unici all'interno della serie o colonna del dataset
print(reviews.country.unique())

# per sapere con quale frequenza appaiono dei valori
print(reviews.country.value_counts())

# posso mappare colonna del data frame, ovvero una serie
# usando .map() oppure .apply()

# .map(trasformazione) , la trasformazione può essere una funzione o specifica
# s.map({'cat': 'kitten', 'dog': 'puppy'})

# apply() si usa invece per trasformare un intero DataSet

# possiamo usare anche i soliti operatori come = > < >= <=



# What is the median of the points column in the reviews DataFrame?
# median_points = reviews.points.median()

# What countries are represented in the dataset? (Your answer should not include any duplicates.)
# countries = reviews.country.unique()

# How often does each country appear in the dataset? 
# Create a Series reviews_per_country mapping countries to the count of reviews of wines from that country.
# reviews_per_country = reviews.country.value_counts()

#Create variable `centered_price` containing a version of the `price` column with the mean price subtracted.
# (Note: this 'centering' transformation is a common preprocessing step before applying various machine learning algorithms.) 
# centered_price = reviews.price.map(lambda p: p - reviews.price.mean())
# row = (reviews.points/reviews.price).idxmax()
# bargain_wine = reviews.loc[row,'title']
# la funzione .idxmax() ritorna il valore dell'indice (riga) del valore massimo di una serie

# There are only so many words you can use when describing a bottle of wine.
#  Is a wine more likely to be "tropical" or "fruity"?
# Create a Series descriptor_counts counting how many times each of these two words appears in the description column in the dataset.
# n_tropical = reviews.description.map(lambda description: 'tropical' in description).sum()
# n_fruity = reviews.description.map(lambda description: 'fruity' in description).sum()
# description_counts = pd.Series([n_tropical,n_fruity],index=['tropical','fruity'])
# print(description_counts)

# We'd like to host these wine reviews on our website, but a rating system ranging from 80 to 100 points is too hard to understand - we'd like to translate them into simple star ratings.
# A score of 95 or higher counts as 3 stars, a score of at least 85 but less than 95 is 2 stars. Any other score is 1 star.
# Also, the Canadian Vintners Association bought a lot of ads on the site, so any wines from Canada should automatically get 3 stars, regardless of points.
# Create a series star_ratings with the number of stars corresponding to each review in the dataset.
'''
def star_rater (row):
    if row.country == 'Canada':
        return 3
    elif row.points >= 95:
        return 3
    elif row.points >= 85:
        return 2
    else:
        return 1

star_ratings = reviews.apply(star_rater,axis='columns')
'''

# .groupby() divide in base a ciò che vogliamo
# reviews.groupby('points').points.count() = reviews.points.value_counts()
reviews = pd.read_csv('winemag-data-130k-v2.csv')
print(reviews)
print(reviews.groupby('points').price.count())

# puoi raggruppare per più parametri
# reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])

# .agg() permette invece di usare più funzioni

print(reviews.groupby(['country']).price.max())

print(reviews.groupby(['country']).points.agg([len,min,max]))

# se uso groupby in alcuni casi creo un multi-index
# lavorare con il multi-index è molto complicato, quindi spesso si riporta a index normale usando la funzione reset_index()
countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])
countries_reviewed.reset_index()


# posso ordinare dopo aver diviso per gruppi
# per ordinare per valore: sort_values(by='nomeColonna') ad es countries_reviewed.sort_values(by='len')
# di default va dal minore al maggiore, se volgio fare al contrario: sort_values(by='nomeColonna', ascending=False)
# per ordinare per indice: sort_index()

# posso ordinare anche per più colonne alla volta as esempio countries_reviewed.sort_values(by=['country', 'len'])


# TIPI DI DATO
# type() ritorna il tipo di oggetto tipo <class 'pandas.core.frame.DataFrame'>
# .dtype ritorna invece il tipo di dato dei valori di una colonna del dataframe 
# mentre per ottenere i tipi di dato dell'interno dataframe, ovvero di tutte le sue colonne, faccio .dtypes (con la s finale del plurale)
print(reviews.points.dtype)
print(reviews.dtypes)

# posso modificare il tipo di dato, usando .astype()
reviews = pd.read_csv('winemag-data-130k-v2.csv')
reviews.points.astype('float64')
print(reviews.head)

# anche l'indice ha un suo tipo:
print(reviews.index.dtype)

# se un dato è mancante, si considera di tipo NaN, ovvero 'not a number', considerato di tipo 'float64'
# per selezione i dati di tipo Nan si usano isnull() e notnull()
print(reviews[pd.isnull(reviews.country)])
print(reviews[pd.notnull(reviews.country)])

a = reviews[pd.notnull(reviews.country)]
print(len(a.index))

# se abbiamo un dato vuoto possiamo riempire con il metodo .fillna()
# ad esempio 
reviews.points.fillna('Unknown')

# oppure possiamo usare il metodo .replace() anche per valori non vuoti
# se cambia il nickname twitter di uno:
reviews.taster_twitter_handle.replace("@kerinokeefe", "@kerino")
# può anche essere utile se ho unkown e voglio cambiarlo o robe del genere


# per rinominare colonne o righe si usa .rename()
# ad esempio
reviews.rename(columns={'points': 'score'})
# mentre per rinominare più elementi
reviews.rename(index={0: 'firstEntry', 1: 'secondEntry'})
print(reviews)
# se devo solo stampare basta così, se devo modificare devo mettere inplace = True

# per rinominare colonne o righe:
reviews.rename_axis("wines", axis='rows').rename_axis("fields", axis='columns')
print(reviews)



# posso combinare datasets con dei metodi: concat(), join() e merge()

# concat semplicemente unisce due dataframe
# esempio:
'''
canadian_youtube = pd.read_csv("../input/youtube-new/CAvideos.csv")
british_youtube = pd.read_csv("../input/youtube-new/GBvideos.csv")

pd.concat([canadian_youtube, british_youtube])
'''

# join serve per concatenare dataframe con index in comune
# ad esempio, per combinare video che erano tren nello stesso giorno
'''.
left = canadian_youtube.set_index(['title', 'trending_date'])
right = british_youtube.set_index(['title', 'trending_date'])
left.join(right, lsuffix='_CAN', rsuffix='_UK')
'''
# lsuffix e rsuffix servono perchè i due dataset hanno lo stesso nome delle colonne in questo caso