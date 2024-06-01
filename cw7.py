import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")
exercise = sns.load_dataset("exercise")

# Zadanie 6.1
Nazwa_rzeki = np.array(['Amazonka', 'Nil', 'Jangcy', 'Missisipi-Missouri', 'Huang He', 'Ob Irtysz', 'Kongo',
                        'Mekong', 'Amur', 'Lena', 'Parana', 'Mackanzie', 'Niger', 'Jenisej', 'Wołga'])
Kontynent = np.array(['Ameryka Poludniowa', 'Afryka', 'Eurazja', 'Ameryka Polnocna', 'Eurazja', 'Eurazja', 'Afryka',
                      'Eurazja', 'Eurazja', 'Eurazja', 'Ameryka Poludniowa', 'Ameryka Polnocna', 'Afryka',
                      'Eurazja', 'Eurazja'])
Dlugosc = np.array([7040, 6695, 6300, 6020, 5464, 5410, 4700, 4500, 4440, 4400, 4380, 4240, 4160, 4102, 3530])
Powierzchnia_dorzecza = np.array([7200, 2870, 1807, 3229, 752, 2972, 3690, 810, 1855, 2490, 3100, 1760, 2117, 2580, 1360])
Liczba_panstw_przez_ktore_przeplywa = np.array([3, 7, 1, 1, 1, 3, 3, 6, 3, 1, 3, 1, 4, 2, 2])

# Ile rzek w tabelce
print(len(Nazwa_rzeki))

# Ktore rzeki przeplywaja przez dokladnie 3 panstwa
print(Nazwa_rzeki[Liczba_panstw_przez_ktore_przeplywa == 3])

# Ile rzek ma dlugosc mniej niz 500
print(len(Nazwa_rzeki[Dlugosc < 5000]))

# Nazwy rzek zaczynajace sie od 'M'
nazwa = Nazwa_rzeki[(Nazwa_rzeki < 'N') & (Nazwa_rzeki >= 'M')]
print(nazwa)

# Posortuj nazwy rzek wg powierzchni malejaco
print(np.sort(Powierzchnia_dorzecza))

# Nazwy rzek z powierzchnia wieksza niz 2000tys km^2, ktore sa w Ameryce(Polnocnej i Poludniowej)
d1 = Nazwa_rzeki[(Powierzchnia_dorzecza>=2000) * (Kontynent == 'Ameryka Polnocna')]
d2 = Nazwa_rzeki[(Powierzchnia_dorzecza>=2000) * (Kontynent == 'Ameryka Poludniowa')]
print(d1, d2)


# Zadanie 6.2
x = np.linspace(0, 1)
y1 = x**2
y2 = np.sqrt(2*x)
fig, ax = plt.subplots(1, 2)
ax[0].plot(x, y1, label="x^2", linestyle="-", color="darkred")
ax[0].set_ylim(0, 1)
ax[1].plot(x, y2, label="sqrt(2x", linestyle=":", color="darkblue")
ax[1].set_ylim(0, 1)
fig.legend(title='Wykres', loc=7)
plt.show()

# Zadanie 6.3
titanic = pd.read_csv('titanic.csv', sep=',')
# Ile kobiet z pierwszej klasy przezylo
print(len(titanic[(titanic['survived'] == 1) & (titanic['pclass'] == 1)]))

# Jaki byl sredni wiek mezczyzn, ktorzy nie przezyli
Wiek = titanic[(titanic['survived'] == 0) & (titanic['sex'] == 'male')]['age'].mean().round(2)
print(Wiek)

# Wykres punktowy
kolory = np.where(titanic['sex'] == 'male', 'b', 'r').tolist()
wiek = titanic['age']
oplata = titanic['fare']
plt.scatter(wiek, oplata, c=kolory)
plt.show()

# Wykres slupkowy
przezyli = titanic['survived']
klasa = titanic['class']
plt.bar(klasa, przezyli)
plt.show()


# Zadanie 6.4
attention = sns.load_dataset("attention")
sns.catplot(data=attention, kind="boxen", x="subject", y="score", palette=['skyblue', 'blue'], hue="attention")
plt.show()
