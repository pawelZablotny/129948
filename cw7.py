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


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Zad1
# Za pomocą biblioteki matplotlib utwórz wykres liniowy funkcji f(x) = sin(x) * x, dla x z przedziału [-3,3] z wartościami zmieniającymi się co 1/2.
# Ustaw zakres osi x na wartości -3 i 3, dodaj etykiety do osi x i y, ustaw tytuł wykresu
# def f(x):
#     return np.sin(x) * x
#
# x_wart = np.arange(-3, 3.5, 0.5)
# y_wart = f(x_wart)
#
# plt.figure(figsize=(10, 6))
# plt.plot(x_wart, y_wart, marker='o')
#
# plt.xlim(-3, 3)
#
# plt.xlabel('x')
# plt.ylabel('f(x) = sin(x) * x')
# plt.title('Wykres funkcji f(x) = sin(x) * x')
#
# plt.grid(True)
# plt.show()

#Zad2
# Za pomocą biblioteki pomocą pandas wczytaj zawartość pliku „automobile.csv” do ramki danych, a następnie:
#	Utwórz i wyświetl nową ramkę danych składającą się z rekordów dla samochodów audi i dodge.
#	Na nowej ramce danych dokonaj grupowania danych po kolumnie „Car model” a następnie policz sumę wartości dla tych samochodów (kolumna Price)
#	Na podstawie utworzonej grupy utwórz wykres słupkowy, dodaj tytuł oraz etykiety dla osi x i y. Dopasuj rozmiar wykresu tak aby był on widoczny w całości.


# df = pd.read_csv('automobile.csv', header=0, sep=';', decimal='.')
#
# filtered_df = df[df['Car model'].isin(['audi', 'dodge'])]
#
# grouped_df = filtered_df.groupby('Car model')['Price'].sum().reset_index()
#
# print("Nowa ramka danych audi i dodge:\n", filtered_df)
# print(grouped_df)
#
# plt.figure(figsize=(12, 8))
# plt.bar(grouped_df['Car model'], grouped_df['Price'], color=['blue', 'green'])
#
# plt.title('Sum of Prices for Audi and Dodge Car Models')
# plt.xlabel('Car Model')
# plt.ylabel('Total Price')
#
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()


#Zad3
# Za pomocą biblioteki pomocą pandas wczytaj zawartość pliku „automobile.csv” do ramki danych i  utwórz wykres kołowy przedstawiający procentową ilość samochodów
# z danym rodzajem paliwa (kolumna Fuel-type). Procentowe wartości mają być zaokrąglone do dwóch miejsc po przecinku, rozmiar czcionki 14. Dodaj tytuł i legendę.

# df = pd.read_csv('automobile.csv', header=0, sep=';', decimal='.')
#
# fuel_counts = df['Fuel-type'].value_counts()
#
# fuel_percentages = (fuel_counts / fuel_counts.sum()) * 100
# fuel_percentages = fuel_percentages.round(2)
#
# plt.figure(figsize=(10, 7))
# plt.pie(fuel_percentages, labels=fuel_percentages.index, autopct='%1.2f%%', textprops={'fontsize': 14})
#
# plt.title('Procentowy podział rodzajów paliwa', fontsize=16)
# plt.legend(fuel_percentages.index, title="Rodzaj paliwa", fontsize=14)
#
# plt.show()